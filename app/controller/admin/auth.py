from flask import render_template
from app.controller.admin import admin





@admin.route('/admin', methods=['GET', 'POST'])
def index():
    return render_template('admin/index.html')

