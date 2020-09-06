# -*- coding: utf-8 -*
# Author: Alex Cater
"""
# @Author  ：Alex Cater
# @Time    : 2020/8/15 1:32
# @File    ： models.py
"""
import datetime

from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {"useexisting": True}
    extend_existing = True
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(100), unique=True)  # 名字
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(100), unique=True)  # 手机号
    info = db.Column(db.Text)  # 签名
    face = db.Column(db.String(100), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    __table_args__ = {"useexisting": True}
    extend_existing = True
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 添加时间

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    __table_args__ = {"useexisting": True}
    extend_existing = True
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 角色权限列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 添加时间
    admins = db.relationship("Admin", backref='role')  # 管理员外键关系关联

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    __table_args__ = {"useexisting": True}
    extend_existing = True
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(100))  # 管理员密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员，0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 添加时间
    adminlogs = db.relationship("Adminlog", backref='admin')  # 管理员登录日志外键关系关联
    oplogs = db.relationship("Oplog", backref='admin')  # 管理员操作日志外键关系关联

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 登录日志
class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    __table_args__ = {"useexisting": True}
    extend_existing = True
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 登录时间

    def __repr__(self):
        return '<Adminlog %r>' % self.id


# 操作日志
class Oplog(db.Model):
    __tablename__ = 'oplog'
    __table_args__ = {"useexisting": True}
    extend_existing = True
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录ip
    reason = db.column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)  # 登录时间

    def __repr__(self):
        return '<Oplog %r>' % self.id


if __name__ == '__main__':
    db.create_all()
