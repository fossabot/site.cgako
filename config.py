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

#Путь до папки с аватарами пользователей
#AVATARS_FOLDER = os.path.join(BASEDIR, 'app/static/admin/upload/users')

#Путь до папки и урл изображений новости
#NEWS_IMAGES_FOLDER_ROOT = os.path.join(BASEDIR, 'app/static/work/uploads/images')
#NEWS_IMAGES_FOLDER_URL =  'work/uploads/images/'

#Настройка тамб-ов для изображений новости
#Директория с исходными изображениями и урл
#THUMBNAIL_MEDIA_ROOT = os.path.join(BASEDIR, 'app/static/work/uploads/images')
#THUMBNAIL_MEDIA_URL = '/static/work/uploads/images'
#Директория для сохранения тамбов
#THUMBNAIL_MEDIA_THUMBNAIL_ROOT = os.path.join(BASEDIR, 'app/static/work/uploads/thumbnails')
#THUMBNAIL_MEDIA_THUMBNAIL_URL = '/static/work/uploads/thumbnails'
#THUMBNAIL_STORAGE_BACKEND = 'flask_thumbnails.storage_backends.FilesystemStorageBackend'
#THUMBNAIL_DEFAUL_FORMAT = 'JPEG'

#Путь до папки с файлами бэкапов
#BACKUPS_FOLDER = os.path.join(basedir, 'app/static/backups')
