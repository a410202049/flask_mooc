# coding: utf-8
from flask import render_template,flash,redirect,request,url_for
from app.controller.admin import admin
from app.controller.admin.forms import LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required,current_user
from app.utils.Auth import Auth
@admin.route('/admin', methods=['GET', 'POST'])
@login_required
def index():
    auth = Auth(current_user)  # 权限验证工具类
    menus = auth.auth_menus()
    return render_template('admin/index.html',menus=menus)

@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            if not user.status:
                #禁止被禁用的用户登陆
                flash('The user has been disabled')
            elif user.is_manage != '1':
                flash('You\'re not an system administrator')
            else:
                login_user(user, form.remember_me.data)
                return redirect(request.args.get('next') or url_for('admin.index'))
        else:
            flash('Invalid username or password.')
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html', form=form)

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('admin.login'))