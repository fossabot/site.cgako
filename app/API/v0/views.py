#! env/bin/python3.6
# -*- coding: utf8 -*-

"""Представления API версии 0. Содержит следующие представления: Пользователи,
Новости"""

import jwt

import traceback

from datetime import datetime, timedelta

from urllib.parse import urljoin

from flask import current_app, json, Blueprint, \
    request, Response, url_for, abort

from functools import wraps

from app import db
from app.models import CmsUsers, CmsUsersSchema

API0 = Blueprint('API0', __name__)

# ------------------------------------------------------------
# Декораторы
# ------------------------------------------------------------


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {'type': 'error',
                       'text': 'Некорректный токен. Требуется регистрация или переданы \
неверные аутентификационные данные.',
                       'authenticated': False}
        expired_msg = {'type': 'error',
                       'text': 'Токен просрочен. Аутентифицируйтесь заново.',
                       'authenticated': False}

        if len(auth_headers) != 2:
            response = Response(
                response=json.dumps(invalid_msg),
                status=401,
                mimetype='application/json'
            )
            return response

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = CmsUsers.query.filter_by(login=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            response = Response(
                response=json.dumps(expired_msg),
                status=401,
                mimetype='application/json'
            )
            return response
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            response = Response(
                response=json.dumps(invalid_msg),
                status=401,
                mimetype='application/json'
            )
            return response

    return _verify


# ------------------------------------------------------------
# Функции
# ------------------------------------------------------------


def server_error(dbg=None):
    """Вывод серверной ошибки с трейсом. Параметр dbg отвечает за вывод
    в формате traceback."""

    if dbg is not None:
        text = traceback.format_exc()
    else:
        text = "Серверная ошибка!"

    response = Response(
        response=json.dumps({'type': 'error', 'text': text}),
        status=500,
        mimetype='application/json'
    )

    return response


def pagination_of_list(query_result, url, start, limit):
    """ Пагинация результатов запроса. Принимает параметры:
    результат запроса (json), URL API для генерации ссылок, стартовая позиция,
    количество выводимых записей"""

    records_count = len(query_result)

    if records_count < start:       # Проверка существования страницы
        abort(404)                  # Сделать адекватную обработку

    response_obj = {}
    response_obj['start'] = start
    response_obj['limit'] = limit
    response_obj['count'] = records_count

    # Создаем URL на предыдущую страницу
    if start == 1:
        response_obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)  # Странный просчет последней стр
        limit_copy = start - 1
        response_obj['previous'] = urljoin(url,
                                           '?start=%d&limit=%d'
                                           % (start_copy, limit_copy))

    # Создаем URL на следующую страницу
    if start + limit > records_count:
        response_obj['next'] = ''
    else:
        start_copy = start + limit
        response_obj['next'] = urljoin(url,
                                       '?start=%d&limit=%d'
                                       % (start_copy, limit))

    # Отсеивание результатов запроса
    response_obj['results'] = query_result[(start - 1):(start - 1 + limit)]

    return response_obj


# ------------------------------------------------------------
# Логин
# ------------------------------------------------------------

@API0.route('/login', methods=['POST'])
def login():
    """Функция логина пользователя, создание JWT-токена"""

    try:

        login_data = request.get_json()

        user = CmsUsers.authenticate(**login_data)
        print(user)

        if not user[0]:

            response = Response(
                response=json.dumps({'type': 'error',
                                     'text': user[1],
                                     'field': user[2],
                                     'authenticated': False}),
                status=401,
                mimetype='application/json'
            )

            return response

        token = jwt.encode({
                            'sub': user[0].login,
                            'iat': datetime.utcnow(),
                            'exp': datetime.utcnow() + timedelta(minutes=30)
                           },
                           current_app.config['SECRET_KEY'])

        response = Response(
            response=json.dumps(token.decode('utf-8')),
            status=200,
            mimetype='application/json'
        )

    except Exception:

        response = server_error(request.args.get("dbg"))

    return response


# ------------------------------------------------------------
# Администрирование пользователей
# ------------------------------------------------------------

@API0.route('/users', methods=['GET'])
@token_required
def get_users(current_user):
    """ Получение полного списка пользователей в json"""

    try:

        user_schema = CmsUsersSchema(many=True)

        users = CmsUsers.query.all()
        udata = user_schema.dump(users)
        udata = udata.data

        udata = pagination_of_list(
            udata,
            url_for('API0.get_users',
                    _external=True),
            start=int(request.args.get('start', 1)),
            limit=int(request.args.get('limit',
                                       current_app.config['LIMIT']))
        )

        response = Response(
            response=json.dumps(udata),
            status=200,
            mimetype='application/json'
        )

    except Exception:

        response = server_error(request.args.get("dbg"))

    return response


@API0.route('/users/<int:uid>', methods=['GET'])
@token_required
def get_user_by_id(current_user, uid):
    """ Получение одного пользователя по id в json"""

    try:

        user_schema = CmsUsersSchema()
        user = CmsUsers.query.get(uid)
        udata = user_schema.dump(user)

        response = Response(
            response=json.dumps(udata.data),
            status=200,
            mimetype='application/json'
        )

    except Exception:

        response = server_error(request.args.get("dbg"))

    return response


@API0.route('/users', methods=['POST'])
@token_required
def post_users(current_user):
    """ Добавление записи пользователя в БД"""

    try:

        post_data = request.get_json()

        exist = CmsUsers.query.filter(
            (CmsUsers.login == post_data['login']) |
            (CmsUsers.email == post_data['email']) |
            (CmsUsers.phone == post_data["phone"])).first()

        if exist:
            response = Response(
                response=json.dumps({'type': 'error',
                                     'text': 'Пользователь с такими данными \
существует!'}),
                status=422,
                mimetype='application/json'
            )
        else:
            user = CmsUsers(
                login=post_data['login'],
                password=post_data['password'],
                name=post_data['name'],
                surname=post_data['surname'],
                patronymic=post_data['patronymic'],
                birth_date=post_data['birth_date'],
                email=post_data['email'],
                phone=post_data["phone"]
            )

            db.session.add(user)
            db.session.commit()

            response = Response(
                response=json.dumps({'type': 'success',
                                     'text': 'Успешно добавлен пользователь \
с id='+str(user.id)+'!',
                                     'link': url_for('.get_user_by_id',
                                                     uid=user.id,
                                                     _external=True)}),
                status=200,
                mimetype='application/json'
            )

    except Exception:

        response = server_error(request.args.get("dbg"))

    return response


@API0.route('/users/<int:uid>', methods=['PUT'])
@token_required
def update_users(current_user, uid):
    """ Изменение записи пользователя в БД"""

    try:

        update_data = request.get_json()

        check = CmsUsers.query.filter(
            (CmsUsers.login == update_data['login']) |
            (CmsUsers.email == update_data['email']) |
            (CmsUsers.phone == update_data["phone"])).first()

        if check.id != uid:
            response = Response(
                response=json.dumps({'type': 'error',
                                     'text': 'Пользователь с такими данными \
существует!'}),
                status=422,
                mimetype='application/json'
            )
        else:
            CmsUsers.query.filter_by(id=uid).update(update_data)
            db.session.commit()

            response = Response(
                response=json.dumps({'type': 'success',
                                     'text': 'Успешно обновлен пользователь \
с id='+str(uid)+'!',
                                     'link': url_for('.get_user_by_id',
                                                     uid=uid,
                                                     _external=True)}),
                status=200,
                mimetype='application/json'
            )

    except Exception:

        response = server_error(request.args.get("dbg"))

    return response


@API0.route('/users/<int:uid>', methods=['DELETE'])
@token_required
def delete_users(current_user, uid):
    """ Удаление записи пользователя из БД"""

    try:

        user = CmsUsers.query.get(uid)

        db.session.delete(user)
        db.session.commit()

        response = Response(
            response=json.dumps({'type': 'success',
                                 'text': 'Успешно удалено!'}),
            status=200,
            mimetype='application/json'
        )

    except Exception:

        response = server_error(request.args.get("dbg"))

    return response

# ------------------------------------------------------------
# Новости
# ------------------------------------------------------------
