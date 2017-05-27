from flask import Blueprint

admin = Blueprint('admin', __name__)

from app.controller.admin import auth
# from app.models import MenuAuth

# @admin.app_context_processor
# def menus():
#     menus = MenuAuth.query.all()
#     return dict(menus=menus)