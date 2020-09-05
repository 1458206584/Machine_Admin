# -*- coding: utf-8 -*
#Author: Alex Cater
"""
# @Author  ：Alex Cater
# @Time    : 2020/8/14 21:36
# @File    ： views.py
"""
from . import admin
from flask import render_template,redirect
@admin.route('/index/')
def index():
    return render_template('admin/index.html')

@admin.route('/')
def login():
    return render_template('admin/login.html')
@admin.route('/register/')
def register():
    return render_template('admin/login.html')

@admin.route('/daily/')
def daily():
    return render_template('admin/daily.html')

