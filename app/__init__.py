# coding: utf-8
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
import datetime
from flask import render_template, request, jsonify

mail = Mail()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app.controller.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')


    @app.errorhandler(403)
    def forbidden(e):
        if request.accept_mimetypes.accept_json and \
                not request.accept_mimetypes.accept_html:
            response = jsonify({'error': 'forbidden'})
            response.status_code = 403
            return response
        return render_template('403.html'), 403


    @app.errorhandler(404)
    def page_not_found(e):
        if request.accept_mimetypes.accept_json and \
                not request.accept_mimetypes.accept_html:
            response = jsonify({'error': 'not found'})
            response.status_code = 404
            return response
        return render_template('404.html'), 404


    @app.errorhandler(500)
    def internal_server_error(e):
        if request.accept_mimetypes.accept_json and \
                not request.accept_mimetypes.accept_html:
            response = jsonify({'error': 'internal server error'})
            response.status_code = 500
            return response
        return render_template('500.html'), 500

    @app.template_filter("omit")
    def omit(data, length):
        if len(data) > length:
            return data[:length-3] + '...'
        return data

    @app.template_filter("friendly_time")
    def friendly_time(date):
        delta = datetime.now() - date
        if delta.days >= 365:
            return u'%d年前' % (delta.days / 365)
        elif delta.days >= 30:
            return u'%d个月前' % (delta.days / 30)
        elif delta.days > 0:
            return u'%d天前' % delta.days
        elif delta.seconds < 60:
            return u"%d秒前" % delta.seconds
        elif delta.seconds < 60 * 60:
            return u"%d分钟前" % (delta.seconds / 60)
        else:
            return u"%d小时前" % (delta.seconds / 60 / 60)
    return app
