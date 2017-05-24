# -*- coding:utf-8 -*-
__author__ = 'kerry'

from app import db
from flask_login import UserMixin,AnonymousUserMixin
from app import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for
import hashlib

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    register_time = db.Column(db.DateTime(), default=datetime.utcnow)
    last_time = db.Column(db.DateTime(), default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)
    confirmed = db.Column(db.Boolean, default=False)
    nickname = db.Column(db.String(64))
    # 用于外键的字段
    group_id = db.Column(db.Integer, db.ForeignKey('users_group.id'))
    group = db.relationship('UsersGroup', backref=db.backref('get_users', lazy='dynamic'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now ,onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = hashlib.md5(
            self.email.encode('utf-8')).hexdigest()
        db.session.add(self)
        return True

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            u = User(
                email=forgery_py.internet.email_address(),
                username=forgery_py.internet.user_name(True),
                password=forgery_py.lorem_ipsum.word(),
                nickname=forgery_py.name.full_name()
            )
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()


    def __repr__(self):
        #打印对象所有属性和值
        return '<User>\n'+'\n'.join(['%s:%s' % item for item in self.__dict__.items()])


class AnonymousUser(AnonymousUserMixin):
    pass

class UsersGroup(db.Model):
    __tablename__ = 'users_group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    status = db.Column(db.Boolean, default=True)
    rules = db.Column(db.Text())
    description = db.Column(db.Text())
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now ,onupdate=datetime.now)

    # @staticmethod
    # def insert_roles():
    #     roles = {
    #         'User': (Permission.FOLLOW |
    #                  Permission.COMMENT |
    #                  Permission.WRITE_ARTICLES, True),
    #         'Moderator': (Permission.FOLLOW |
    #                       Permission.COMMENT |
    #                       Permission.WRITE_ARTICLES |
    #                       Permission.MODERATE_COMMENTS, False),
    #         'Administrator': (0xff, False)
    #     }
    #     for r in roles:
    #         role = Role.query.filter_by(name=r).first()
    #         if role is None:
    #             role = Role(name=r)
    #         role.permissions = roles[r][0]
    #         role.default = roles[r][1]
    #         db.session.add(role)
    #     db.session.commit()

    def __repr__(self):
        return '<UsersGroup>\n' + '\n'.join(['%s:%s' % item for item in self.__dict__.items()])

class MenuAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.Integer,default=0)
    name = db.Column(db.String(20))
    controller  = db.Column(db.String(20))
    method = db.Column(db.String(100))
    sort = db.Column(db.Integer, default=0)
    icon = db.Column(db.String(30))











