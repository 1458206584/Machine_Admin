# -*- coding: utf-8 -*
#Author: Alex Cater
"""
# @Author  ：Alex Cater
# @Time    : 2020/8/14 21:33
# @File    ： __init__.py.py
"""
# 导入蓝图
from flask import Blueprint
# 实例化蓝图
admin = Blueprint('admin',__name__)
# 导入views文件
import app.admin.views

