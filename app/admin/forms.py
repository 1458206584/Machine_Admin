# -*- coding: utf-8 -*
# Author: Alex Cater
"""
# @Author  ：Alex Cater
# @Time    : 2020/8/14 21:35
# @File    ： forms.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, SelectField,DateTimeField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from app.models import Admin, Auth, Role,Machineroom,Machine,Platform


class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",

        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",

        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate_account(self, field):
        account = field.data
        # 查询账号并统计有几条
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在！")


class PwdForm(FlaskForm):
    """修改密码表单"""
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("请输入旧密码！")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码！",
        }
    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired("请输入新密码！")
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码！",
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )

    def validate_old_pwd(self, field):
        from flask import session
        pwd = field.data
        name = session["admin"]
        admin = Admin.query.filter_by(
            name=name
        ).first()
        if not admin.check_pwd(pwd):
            raise ValidationError("旧密码错误！")

class MachineForm(FlaskForm):
    name = StringField(
        label="机器名称",
        validators=[
            DataRequired("请输入机器名称！")
        ],
        description="机器名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入机器名称！",
        }
    )
    url = StringField(
        label="机器IP",
        validators=[
            DataRequired("请输入机器IP！")
        ],
        description="机器IP",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入机器IP！",
        }
    )
    CPU = StringField(
        label="CPU型号",
        description="CPU型号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入CPU型号！",
        }
    )
    RAM = StringField(
        label="内存容量",
        validators=[
            DataRequired("请输入内存容量！")
        ],
        description="内存容量",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入内存容量！",
        }
    )
    IPMI = StringField(
        label="IPMI地址",
        validators=[
            DataRequired("请输入IPMI地址！")
        ],
        description="IPMI地址",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入IPMI地址！",
        }
    )
    machineroom_id = SelectField(
        label="所属机房",
        coerce=int,
        choices=[(v.id, v.name) for v in Machineroom.query.all()],
        render_kw={
            "class": "form-control",
        }
    )
    platform_id = SelectField(
        label="所属平台",
        coerce=int,
        choices=[(v.id, v.name) for v in Platform.query.all()],
        render_kw={
            "class": "form-control",
        }
    )
    putontime =  StringField(
        label="上架时间",
        validators=[
            DataRequired("请选择上架时间！")
        ],
        description="上架时间",
        render_kw={
            "class": "form-control",
            "placeholder": "请选择上架时间！",
            "id": "input_release_time"
        }
    )
    submit = SubmitField(
        '提交',
        render_kw={
            "class": "btn btn-primary",
        }
    )



class AuthForm(FlaskForm):
    name = StringField(
        label="权限名称",
        validators=[
            DataRequired("请输入权限名称！")
        ],
        description="权限名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入权限名称！"
        }
    )
    url = StringField(
        label="权限地址",
        validators=[
            DataRequired("请输入权限地址！")
        ],
        description="权限地址",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入权限地址！"
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class RoleForm(FlaskForm):
    name = StringField(
        label="角色名称",
        validators=[
            DataRequired("请输入角色名称！")
        ],
        description="角色名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入角色名称！"
        }
    )
    auths = SelectMultipleField(
        label="权限列表",
        validators=[
            DataRequired("请选择权限列表！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in Auth.query.all()],
        description="权限列表",
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class AdminForm(FlaskForm):
    name = StringField(
        label="管理员名称",
        validators=[
            DataRequired("请输入管理员名称！")
        ],
        description="管理员名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员名称！",
        }
    )
    pwd = PasswordField(
        label="管理员密码",
        validators=[
            DataRequired("请输入管理员密码！")
        ],
        description="管理员密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员密码！",
        }
    )
    repwd = PasswordField(
        label="管理员重复密码",
        validators=[
            DataRequired("请输入管理员重复密码！"),
            EqualTo('pwd', message="两次密码不一致！")
        ],
        description="管理员重复密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员重复密码！",
        }
    )
    role_id = SelectField(
        label="所属角色",
        coerce=int,
        choices=[(v.id, v.name) for v in Role.query.all()],
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )
