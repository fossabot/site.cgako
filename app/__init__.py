#! env/bin/python3.6
# -*- coding: utf8 -*-

"""Инициализация приложения.

Инициализация приложения Flask, объявление блюпринтов,
создание экземпляров библиотек.
"""

from flask import Flask

from flask_cors import CORS

from flask_marshmallow import Marshmallow

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

cors = CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.API.v0.views import API0
# from app.API.v0_1.views import API01 as api_v0_1

migrate = Migrate(app, db)

app.register_blueprint(API0, url_prefix='/API/v0')
# app.register_blueprint(api_v0_1, url_prefix='/API/v0.1')
