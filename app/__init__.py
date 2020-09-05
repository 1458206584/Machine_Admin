# -*- coding: utf-8 -*
# Author: Alex Cater
"""
# @Author  ：Alex Cater
# @Time    : 2020/8/14 21:24
# @File    ： __init__.py.py
"""
# 导入flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import config

# 实例化flask对象
app = Flask(__name__)
app.debug = True
# 导入数据库
app.config.from_object(config)
app.config['SECRET_KEY'] = '0da36d29bab64b17b04556d1b343b547'
db = SQLAlchemy(app)
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(admin_blueprint)

# 导入数据库
app.config.from_object(config)
app.config['SECRET_KEY'] = '0da36d29bab64b17b04556d1b343b547'



# 404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('admin/404.html'), 404
