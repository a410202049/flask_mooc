# coding: utf-8
from flask import render_template,flash
from app.controller.admin import admin
from app.controller.admin.forms import LoginForm
@admin.route('/admin', methods=['GET', 'POST'])
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print u"通过验证"
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user is not None and user.verify_password(form.password.data):
    #         login_user(user, form.remember_me.data)
    #         return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('admin/login.html', form=form)