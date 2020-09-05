# -*- coding: utf-8 -*
#Author: Alex Cater
"""
# @Author  ：Alex Cater
# @Time    : 2020/8/14 21:24
# @File    ： __init__.py.py
"""
# 导入flask
from flask import Flask
# 实例化flask对象
app = Flask(__name__)
app.debug = True
# 导入蓝图实例
from app.admin import admin as admin_blueprint
# 注册蓝图
app.register_blueprint(admin_blueprint)