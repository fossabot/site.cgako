#! env/bin/python3.6
# -*- coding: utf8 -*-

from app import db

class cmsUsers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(32))
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
    
    # def current():
        # if session.get('user_id'):
            # return User.query.filter(User.id == session['user_id']).first()
        # else:
            # return None
            
    # def can(operation, url):
        # user_info = User.current()
        
        # table_id = Table_db.query.filter(Table_db.url == url).first().id
        # perms = Permission.query.filter(((Permission.role_id==user_info.role_id)|(Permission.user_id==user_info.id))&(Permission.table_id == table_id)).all()


        # bool_lst = []
        # temp = False

        # if operation == "enter":
            # for perm in perms:
                # bool_lst.append(perm.enter)
        # if operation == "insert":
            # for perm in perms:
                # bool_lst.append(perm.insert)
        # if operation == "update":
            # for perm in perms:
                # bool_lst.append(perm.update)
        # if operation == "delete":
            # for perm in perms:
                # bool_lst.append(perm.delete)

        # for boolval in bool_lst:
            # temp = temp or boolval
    
        # return temp
        
    # def get_pylist(order="initial_last", fullness="shortened"):
        
        # all_users = User.query.all()
        # name_string = ''
        # rslt_lst = []
        
        # for user in all_users:
            # if fullness == "shortened":
                # name_string = user.name[:1] + "." + user.patronymic[:1]+"."
            # elif fullness == "full":
                # name_string = user.name + " " + user.patronymic
            # if order == "initial_last":
                # name_string = user.surname + " " + name_string
            # elif order == "initial_first":
                # name_string = name_string + " " + user.surname
            
            # rslt_lst.append((user.id, name_string))
        
        # return rslt_lst


    def __repr__(self):
        return 'Пользователь id:%i, имя:%r ' % (self.id, self.name)
