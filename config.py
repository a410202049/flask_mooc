# -*- coding:utf-8 -*-
__author__ = u'kerry'

import os
import hashlib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '\x03d\xf4\x95J\x15\xa4B\xfb\xc0\xaf \xd1A[j$}\x18\x16a\xe7\xd0\xec'
    STRIPE_API_KEY = '\x03d\xf4\x95J\x15\xa4B\xfb\xc0\xaf \xd1A[j$}\x18\x16a\xe7\xd0\xec'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    #所有SQLALCHEMY配置项可参考手册http://www.pythondoc.com/flask-sqlalchemy/config.html#id2
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/flask_mooc?charset=utf8" 


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/flask_mooc?charset=utf8" 


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}