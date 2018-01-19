#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template,request,flash
from conf.Forms import Login_Form
from conf.DbConfig import User
# from flask_login import login_user

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET','POST'])
def index():
    if request.method == "GET":   #check method
        userForm = Login_Form(request.form)

        return render_template("login.html",form=userForm)

    else:
        form = Login_Form(request.form)
        if form.validate():
            user=User.query.filter_by(username=form.UserName.data).first()
            if user is not None and user.password==form.UserPass.data:
                # login_user(user)
                flash(u'登陆成功')
            else:
                flash(u'用户名或密码错误')

            return render_template("login.html",form=form)
        else:
            if form.errors:
                for error in form.errors.values():
                    flash(error[0])

            return render_template("login.html",form=form)

# 'Login_form'
"""
Flask-Login 0.4.1
https://pypi.python.org/packages/c1/ff/bd9a4d2d81bf0c07d9e53e8cd3d675c56553719bbefd372df69bf1b3c1e4/Flask-Login-0.4.1.tar.gz



"""