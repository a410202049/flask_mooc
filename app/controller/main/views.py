from flask import render_template,current_app
from flask_sqlalchemy import get_debug_queries
from app.controller.main import main
from app.models.models import User

@main.after_app_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= current_app.config['FLASKY_SLOW_DB_QUERY_TIME']:
            current_app.logger.warning(
                'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
                % (query.statement, query.parameters, query.duration,
                   query.context))
    return response



@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

