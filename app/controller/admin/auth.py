# coding: utf-8
from flask import render_template,flash,redirect,request,url_for
from app.controller.admin import admin
from app.controller.admin.forms import LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required,current_user

@admin.route('/admin', methods=['GET', 'POST'])
@login_required
def index():
    print current_user
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('admin.index'))
        flash('Invalid username or password.')
    return render_template('admin/login.html', form=form)

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('admin.login'))