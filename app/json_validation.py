#! env/bin/python3.6
# -*- coding: utf8 -*-

"""Модели данных БД."""

import re
import datetime

from jsonschema import validators, Draft4Validator
from jsonschema.exceptions import ValidationError
from validate_email import validate_email

# ------------------------------------------------------------
# Схемы
# ------------------------------------------------------------

#  Профиль пользователя CMS
schema_profile_data = {
    "type": "object",
    "properties": {
        "login": {
                    "type": "string",
                    "pattern": r"\b[a-zA-Z0-9]{4,20}\b",
                    "minLength": 1
                 },
        "name": {
                    "type": "string",
                    "pattern": r'\b[а-яА-Я]{4,20}\b',
                    "minLength": 1
                 },
        "surname": {
                    "type": "string",
                    "pattern": r'\b[а-яА-Я]{4,20}\b',
                    "minLength": 1
                 },
        "patronymic": {
                    "type": "string",
                    "pattern": r'\b[а-яА-Я]{4,20}\b',
                    "minLength": 1
                 },
        "email": {
                    "type": "string",
                    'is_email': True,
                    "minLength": 1
                 },
        "phone": {
                    "type": "string",
                    "pattern": r'(^\+7\s\d{3,3}\s\d{3,3}\s\d{2,2}\s\d{2,2}$)',
                    "minLength": 1
                 },
        "birth_date": {
                    "type": "string",
                    'is_date': True,
                    "minLength": 1
                      },
        "about_me": {
                    "type": "string",
                    "pattern": r'(^.{0,140}$)'
                    },
        "password": {
                    "type": "string",
                    "is_valid": True,
                    "minLength": 1
                    },
    },
    "required": ["login", "email", "phone"],
    "additionalProperties": False
}

schema_profile_password = {
    "type": "object",
    "properties": {
        "login": {
                    "type": "string",
                    "pattern": r"\b[a-zA-Z0-9]{4,20}\b",
                    "minLength": 1
                 },
        "passwordOld": {
                    "type": "string",
                    "minLength": 1
                 },
        "passwordNew": {
                    "type": "string",
                    "is_valid": True,
                    "minLength": 1
                    },
    },
    "required": ["login", "passwordNew", "passwordOld"],
    "additionalProperties": False
}

# ------------------------------------------------------------
# Кастомные валидаторы
# ------------------------------------------------------------


def is_email(validator, value, instance, schema_profile_data):
    if not isinstance(instance, str):
        yield ValidationError("%r not string" % instance)
    if re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
                 instance) is None:
        yield ValidationError("%r not in email format" % (instance))
    elif validate_email(instance, verify=True, check_mx=True) is None:
        yield ValidationError("%r address doesn't exist" % (instance))


def is_date(validator, value, instance, schema_profile_data):
    try:
        datetime.datetime.strptime(instance, '%Y-%m-%d')
    except ValueError:
        yield ValidationError("%r incorrect birth date format" % (instance))


def is_valid(validator, value, instance, schema_profile_password):
    if not isinstance(instance, str):
        yield ValidationError("%r not string" % instance)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeric = '0123456789'
    special = '!@#$%^&*()_+~`|}{[]:;?><,./-='

    occurs = {'alphabet': 0, 'alphabetUpper': 0,
              'numeric': 0, 'special': 0}

    for char in instance:
        if char in alphabet:
            occurs['alphabet'] += 1
        if char in alphabet_upper:
            occurs['alphabetUpper'] += 1
        if char in numeric:
            occurs['numeric'] += 1
        if char in special:
            occurs['special'] += 1

    for key, value in occurs.items():
        if value == 0:
            yield ValidationError(
                "%r incorrect format of password" % (instance))


all_validators = dict(Draft4Validator.VALIDATORS)
all_validators.update({'is_email': is_email, 'is_date': is_date,
                       'is_valid': is_valid})

MyValidator = validators.create(
    meta_schema=Draft4Validator.META_SCHEMA,
    validators=all_validators
)

profile_validator = MyValidator(schema_profile_data)
password_validator = MyValidator(schema_profile_password)
