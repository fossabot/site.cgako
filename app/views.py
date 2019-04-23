#! env/bin/python3.6
# -*- coding: utf8 -*-

from app import app, db
from flask import jsonify

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
