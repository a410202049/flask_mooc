#!/usr/bin/python
# -*- encoding: utf-8 -*-
from app.controller.admin import admin
from flask import render_template
from flask_login import login_required
@admin.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    print '11111111'
    return render_template('admin/dashboard.html')


