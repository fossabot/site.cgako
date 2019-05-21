#! env/bin/python3.6
# -*- coding: utf8 -*-

"""Модели данных БД."""

from app import bcrypt, db, ma


class CmsUsers(db.Model):
    """Модель данных пользователя."""

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(60))
    socials = db.Column(db.JSON(none_as_null=True))
    photo = db.Column(db.String(50))
    name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    patronymic = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(18), unique=True)

    birth_date = db.Column(db.Date)
    last_login = db.Column(db.DateTime)

    status = db.Column(db.SmallInteger)

    # department_id = db.Column(db.Integer,
    # db.ForeignKey("arhiv.department.id"))
    # post_id = db.Column(db.Integer, db.ForeignKey("arhiv.post.id"))
    # role_id = db.Column(db.Integer, db.ForeignKey("arhiv.role.id"))

    # important_news = db.relationship('Important_news',
    # backref = 'user',lazy = 'dynamic')
    # history = db.relationship('History', backref = 'user_parent',
    # lazy = 'dynamic')
    # permission = db.relationship('Permission', backref = 'user',
    # lazy = 'dynamic')
    # news = db.relationship('News', backref = 'user',lazy = 'dynamic')
    # appeals = db.relationship('Appeals', backref = 'user',lazy = 'dynamic')
    # executor = db.relationship('Executor', backref = 'user',lazy = 'dynamic')

    # employee = db.relationship('Item',
    # backref='item_employee',
    # lazy='dynamic',
    # foreign_keys='Item.employee')
    # responsible = db.relationship('Item',
    # backref='item_responsible',
    # lazy='dynamic',
    # foreign_keys='Item.responsible')

    def __init__(self, login, password,
                 name, surname, patronymic,
                 email, phone, birth_date,
                 last_login=None, status=None, socials=None, photo=None):
        """Конструктор класса."""
        self.login = login
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.socials = None if socials is None else socials
        self.photo = None if photo is None else photo
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.last_login = None if last_login is None else last_login
        self.status = 1 if status is None else status

    def __repr__(self):
        """Форматирование представления экземпляра класса."""
        return 'Пользователь id:%i, имя:%r ' % (self.id, self.name)

    @classmethod
    def authenticate(cls, **kwargs):
        """Функция аутентификации."""
        login = kwargs.get('login')
        password = kwargs.get('password')

        if not login or not password:
            return (None, 'Не переданы данные для аутентификации пользователя!', 'empty')

        user = cls.query.filter((cls.login == login) | (cls.email == login)).first()

        if not user:
            return (None, 'Пользователь не найден!', 'username')
        elif not bcrypt.check_password_hash(user.password, password):
            return (None, 'Неверный пароль!', 'password')

        return (user, 'Успешно!')


class CmsUsersSchema(ma.ModelSchema):
    """Marshmallow-схема для перегона модели в json формат."""

    class Meta:
        """Мета модели, вносятся доп. параметры."""

        model = CmsUsers
