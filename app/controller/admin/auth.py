# coding: utf-8
from flask import render_template,flash
from app.controller.admin import admin
from app.controller.admin.forms import LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required,current_user

@admin.route('/admin', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Invalid username or password.')
    return render_template('admin/login.html', form=form)