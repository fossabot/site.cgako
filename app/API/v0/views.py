#! env/bin/python3.6
# -*- coding: utf8 -*-
import sys, traceback

from app import app, db
from flask import json, jsonify, Blueprint, request, Response, url_for

from app.models import cmsUsers
from app.models import cmsUsersSchema

API0 = Blueprint('API0', __name__)

# Функции

# Пагинация

def pagination_of_list(query_result, url, start, limit):
    
    return "OK"

# Пользователи
@API0.route('/users', methods=['GET'])
def get_users():
    try:
        user_schema = cmsUsersSchema(many=True)
        users = cmsUsers.query.all()
        udata = user_schema.dump(users)

        response = Response(
            response=json.dumps(udata.data),
            status=200,
            mimetype='application/json'
        )
        
    except:
        debug = request.args.get("dbg")
        if debug is not None:
            text = traceback.format_exc()
        else:
            text = "Серверная ошибка!"
            
        response = Response(
            response=json.dumps({'type':'error', 'text':text}),
            status=500,
            mimetype='application/json'
        )
    
    return response
    
@API0.route('/users/<int:uid>', methods=['GET'])
def get_user_by_id(uid):

    try:
        user_schema = cmsUsersSchema()
        user = cmsUsers.query.get(uid)
        udata = user_schema.dump(user)

        response = Response(
            response=json.dumps(udata.data),
            status=200,
            mimetype='application/json'
        )
        
    except:
        debug = request.args.get("dbg")
        if debug is not None:
            text = traceback.format_exc()
        else:
            text = "Серверная ошибка!"
            
        response = Response(
            response=json.dumps({'type':'error', 'text':text}),
            status=500,
            mimetype='application/json'
        )
    
    return response

@API0.route('/users', methods=['POST'])
def post_users():

    try:
        post_data = request.get_json()
        
        check = cmsUsers.query.filter((cmsUsers.login==post_data['login'])|(cmsUsers.email==post_data['email'])|(cmsUsers.phone==post_data["phone"])).first()
        
        if check:
            response = Response(
                response=json.dumps({'type':'error', 'text':'Пользователь с такими данными существует!'}),
                status=422,
                mimetype='application/json'
            )
        else:
            user = cmsUsers(
                login = post_data['login'],
                password = post_data['password'],
                name = post_data['name'],
                surname = post_data['surname'],
                patronymic = post_data['patronymic'],
                birth_date = post_data['birth_date'],
                email = post_data['email'],
                phone = post_data["phone"],
                status = post_data["status"]
            )
            
            db.session.add(user)
            db.session.commit()

            response = Response(
                response=json.dumps({'type':'success', 'text':'Успешно добавлено!', 'link':url_for('.get_user_by_id', uid=user.id)}),
                status=200,
                mimetype='application/json'
            )
        
    except:
        debug = request.args.get("dbg")
        if debug is not None:
            text = traceback.format_exc()
        else:
            text = "Серверная ошибка!"
            
        response = Response(
            response=json.dumps({'type':'error', 'text':text}),
            status=500,
            mimetype='application/json'
        )
    
    return response
    
@API0.route('/users/<int:uid>', methods=['PUT'])
def update_users(uid):
    
    try:
        update_data = request.get_json()

        check = cmsUsers.query.filter((cmsUsers.login==update_data['login'])|(cmsUsers.email==update_data['email'])|(cmsUsers.phone==update_data["phone"])).first()
        
        if check.id != uid:
            response = Response(
                response=json.dumps({'type':'error', 'text':'Пользователь с такими данными существует!'}),
                status=422,
                mimetype='application/json'
            )
        else:
            user = cmsUsers.query.filter_by(id=uid).update(update_data)
            db.session.commit()

            response = Response(
                response=json.dumps({'type':'success', 'text':'Успешно обновлен пользователь с id='+str(uid)+'!', 'link':url_for('.get_user_by_id', uid=uid)}),
                status=200,
                mimetype='application/json'
            )
        
    except:
        debug = request.args.get("dbg")
        if debug is not None:
            text = traceback.format_exc()
        else:
            text = "Серверная ошибка!"
            
        response = Response(
            response=json.dumps({'type':'error', 'text':text}),
            status=500,
            mimetype='application/json'
        )
    
    return response
    
@API0.route('/users/<int:uid>', methods=['DELETE'])
def delete_users(uid):

    try:
        user = cmsUsers.query.get(uid)
            
        db.session.delete(user)
        db.session.commit()
        
        response = Response(
            response=json.dumps({'type':'success', 'text':'Успешно удалено!'}),
            status=200,
            mimetype='application/json'
        )
        
    except:
        debug = request.args.get("dbg")
        if debug is not None:
            text = traceback.format_exc()
        else:
            text = "Серверная ошибка!"
            
        response = Response(
            response=json.dumps({'type':'error', 'text':text}),
            status=500,
            mimetype='application/json'
        )
    
    return response
