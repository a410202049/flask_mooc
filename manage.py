# -*- coding:utf-8 -*-
__author__ = 'kerry'

import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User,UsersGroup


app = create_app('default')
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)


def make_shell_context():
    return dict(app=app, db=db,User=User,UsersGroup=UsersGroup)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
