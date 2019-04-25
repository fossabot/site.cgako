#! env/bin/python3.6
# -*- coding: utf8 -*-

from app import app, db
from flask import jsonify

from app.models import cmsUsers
from app.models import cmsUsersSchema

@app.route('/users', methods=['GET'])
def ping_pong():
    
    user_schema = cmsUsersSchema(many=True)
    user = cmsUsers.query.all()
    jdata = user_schema.dump(user)
    
    return jsonify(jdata.data)
