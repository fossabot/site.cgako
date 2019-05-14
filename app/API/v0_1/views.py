#! env/bin/python3.6
# -*- coding: utf8 -*-

# from app import app, db
# from flask import jsonify, Blueprint

# from app.models import cmsUsers
# from app.models import cmsUsersSchema

# API01 = Blueprint('API01', __name__)

# @API01.route('/users', methods=['GET'])
# def get_users():

    # user_schema = cmsUsersSchema(many=True)
    # user = cmsUsers.query.all()
    # udata = user_schema.dump(user)

    # Запрос по JSON полю с фильтром
    # ldata = cmsUsers.query.filter(cmsUsers.socials['yandex']=="1")
    # zdata = user_schema.dump(ldata)

    # return jsonify(udata.data)
