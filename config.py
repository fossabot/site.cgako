#! env/bin/python3.6
# -*- coding: utf8 -*-

import os

# конфигурация
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY="9c1c01dc3ac1445a500251fc34a15d3e75a849df"
JSON_AS_ASCII = False

#базовая директория
BASEDIR = os.path.abspath(os.path.dirname(__file__))

#база данных
SQLALCHEMY_BASIC_URI = 'mysql+pymysql://cgako_administrator:tester@localhost/'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cgako_administrator:tester@localhost/cgako_site_db'
SQLALCHEMY_TRACK_MODIFICATIONS = 'true'
