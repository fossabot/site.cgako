#! env/bin/python3.6
# -*- coding: utf8 -*-

from app import db, ma

class cmsUsers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(32))
    socials = db.Column(db.JsonEncodedDict)
    photo = db.Column(db.String(50))
    name = db.Column(db.String(15))
    surname = db.Column(db.String(15))
    patronymic = db.Column(db.String(15))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(18), unique=True)

    birth_date = db.Column(db.Date)
    last_login = db.Column(db.DateTime)

    status = db.Column(db.SmallInteger)

    # department_id = db.Column(db.Integer, db.ForeignKey("arhiv.department.id"))
    # post_id = db.Column(db.Integer, db.ForeignKey("arhiv.post.id"))
    # role_id = db.Column(db.Integer, db.ForeignKey("arhiv.role.id"))

    # important_news = db.relationship('Important_news', backref = 'user',lazy = 'dynamic')
    # history = db.relationship('History', backref = 'user_parent',lazy = 'dynamic')
    # permission = db.relationship('Permission', backref = 'user',lazy = 'dynamic')
    # news = db.relationship('News', backref = 'user',lazy = 'dynamic')
    # appeals = db.relationship('Appeals', backref = 'user',lazy = 'dynamic')
    # executor = db.relationship('Executor', backref = 'user',lazy = 'dynamic')
    
    # employee = db.relationship('Item', backref = 'item_employee',lazy = 'dynamic', foreign_keys='Item.employee')
    # responsible = db.relationship('Item', backref = 'item_responsible',lazy = 'dynamic', foreign_keys='Item.responsible')


    def __repr__(self):
        return 'Пользователь id:%i, имя:%r ' % (self.id, self.name)
        
#Marshmallow схемы
class cmsUsersSchema(ma.ModelSchema):
    class Meta:
        model = cmsUsers
