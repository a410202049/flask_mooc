#!/usr/bin/python
# -*- encoding: utf-8 -*-
from app.models import MenuAuth

class base(object):
    def __init__(self):
        self.menus = []
        menus = MenuAuth.query.first()


