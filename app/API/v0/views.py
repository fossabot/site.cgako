#! env/bin/python3.6
# -*- coding: utf8 -*-

from app import app, db
from flask import json, jsonify, Blueprint, request, Response

from app.models import cmsUsers
from app.models import cmsUsersSchema

API0 = Blueprint('API0', __name__)

#Пользователи
@API0.route('/users', methods=['GET'])
def get_users():
    
    try:
        user_schema = cmsUsersSchema(many=True)
        user = cmsUsers.query.all()
        udata = user_schema.dump(user)

        response = Response(
            response=json.dumps(udata),
            status=200,
            mimetype='application/json'
        )
        
    except:
        response = Response(
            response=json.dumps({'type':'error', 'text':'Серверная ошибка!'}),
            status=500,
            mimetype='application/json'
        )
    
    return response
    
@API0.route('/users/<int:uid>', methods=['GET'])
def get_users_by_id(uid):

    try:
        user_schema = cmsUsersSchema()
        user = cmsUsers.query.get(uid)
        udata = user_schema.dump(user)

        response = Response(
            response=json.dumps(udata),
            status=200,
            mimetype='application/json'
        )
        
    except:
        response = Response(
            response=json.dumps({'type':'error', 'text':'Серверная ошибка!'}),
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
            users = cmsUsers(
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
            
            db.session.add(users)
            db.session.commit()
            
            response = Response(
                response=json.dumps({'type':'success', 'text':'Успешно добавлено!'}),
                status=200,
                mimetype='application/json'
            )
        
    except:
        response = Response(
            response=json.dumps({'type':'error', 'text':'Серверная ошибка!'}),
            status=500,
            mimetype='application/json'
        )
    
    return response
    
# @API0.route('/users', methods=['UPDATE'])
# def update_users():
    
    # user_schema = cmsUsersSchema(many=True)
    # user = cmsUsers.query.all()
    # udata = user_schema.dump(user)

    # return jsonify(udata.data)
    
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
        response = Response(
            response=json.dumps({'type':'error', 'text':'Серверная ошибка!'}),
            status=500,
            mimetype='application/json'
        )
    
    return response
