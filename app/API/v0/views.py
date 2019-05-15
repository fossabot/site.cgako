#! env/bin/python3.6
# -*- coding: utf8 -*-

"""Представления API версии 0. Содержит следующие представления: Пользователи,
Новости"""

import traceback
from urllib.parse import urljoin

from flask import json, Blueprint, request, Response, url_for, abort

from app import db
from app.models import CmsUsers, CmsUsersSchema

from config import LIMIT

API0 = Blueprint('API0', __name__)

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
# Пользователи
# ------------------------------------------------------------


@API0.route('/users', methods=['GET'])
def get_users():
    """ Получение полного списка пользователей в json"""

    try:

        all_records = request.args.get("all")

        user_schema = CmsUsersSchema(many=True)
        users = CmsUsers.query.all()
        udata = user_schema.dump(users)
        udata = udata.data

        if all_records is None:
            udata = pagination_of_list(udata,
                                       url_for('API0.get_users',
                                               _external=True),
                                       start=int(request.args.get('start', 1)),
                                       limit=int(request.args.get('limit',
                                                                  LIMIT))
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
def get_user_by_id(uid):
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
def post_users():
    """ Добавление записи пользователя в БД"""

    try:

        post_data = request.get_json()

        check = CmsUsers.query.filter(
            (CmsUsers.login == post_data['login']) |
            (CmsUsers.email == post_data['email']) |
            (CmsUsers.phone == post_data["phone"])).first()

        if check:
            response = Response(
                response=json.dumps({'type': 'error',
                                     'text': 'Пользователь с такими данными\
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
                phone=post_data["phone"],
                status=post_data["status"]
            )

            db.session.add(user)
            db.session.commit()

            response = Response(
                response=json.dumps({'type': 'success',
                                     'text': 'Успешно добавлен пользователь\
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
def update_users(uid):
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
                                     'text': 'Пользователь с такими данными\
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
def delete_users(uid):
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
