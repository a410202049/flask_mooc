from flask import render_template,current_app
from flask_sqlalchemy import get_debug_queries
from app.controller.home import home


@home.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home/index.html')

