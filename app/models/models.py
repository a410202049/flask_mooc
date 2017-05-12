# -*- coding:utf-8 -*-
__author__ = 'kerry'


from app import db
from flask_login import UserMixin
from app import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = 'kerry'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    # status = db.Column(db.Boolean, default=False)
    # role = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return '<User %r>' % self.username











