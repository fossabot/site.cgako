#! env/bin/python3.6
# -*- coding: utf8 -*-

"""Конфигурационный файл бэкенда."""

import os

# Конфигурация
DEBUG = True
CSRF_ENABLED = True
JSON_AS_ASCII = False

# Базовая директория
BASEDIR = os.path.abspath(os.path.dirname(__file__))
CMS_USERS_AVATARS = os.path.join(BASEDIR, 'client/static/profile_avatars/')

# Соединение с БД
SQLALCHEMY_BASIC_URI = 'mysql+pymysql://cgako_administrator:tester@localhost/'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cgako_administrator:tester@localhost/\
cgako_site_db'
SQLALCHEMY_TRACK_MODIFICATIONS = 'true'

# Умолчания
LIMIT = 20  # Количество записей в пагинированном json

# Аутентификация
SECRET_KEY = "9c1c01dc3ac1445a500251fc34a15d3e75a849df" # Ключ
TOKEN_DURATION = 1 # Длительность валидности токена в днях
