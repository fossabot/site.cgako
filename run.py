#! env/bin/python3.6
# -*- coding: utf8 -*-

"""Файл запуска приложения Flask"""

from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0")
