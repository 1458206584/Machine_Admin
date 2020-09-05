# -*- coding: utf-8 -*
# Author: Alex Cater
"""
# @Author  ：Alex Cater
# @Time    : 2020/8/14 21:36
# @File    ： views.py
"""
from functools import wraps

from flask import render_template, redirect, url_for, flash, session, request

from admin.forms import LoginForm
from app.models import Admin
from . import admin


# 登录装饰器
def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@admin.route('/index/')
@admin_login_req
def index():
    return render_template('admin/index.html')


# 登录
@admin.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！", 'err')
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]
        session["admin_id"] = admin.id
        # adminlog = Adminlog(
        #     admin_id=admin.id,
        #     ip=request.remote_addr,
        # )
        # db.session.add(adminlog)
        # db.session.commit()
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template('admin/login.html', form=form)


# 退出
@admin.route('/logout/')
def logout():
    session.pop('admin', None)
    return redirect(url_for("admin.login"))


@admin.route('/register/')
def register():
    return render_template('admin/login.html')


@admin.route('/daily/')
def daily():
    return render_template('admin/daily.html')
