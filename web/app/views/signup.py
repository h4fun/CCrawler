#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template,request,flash
from conf.Forms import RegistForm
from conf.DbConfig import User,db

signup = Blueprint('signup', __name__)

@signup.route('/signup', methods=['GET','POST'])
def index():
    if request.method == "GET":   #check method
        form = RegistForm(request.form)

        return render_template("signup.html",form=form)

    else:
        form = RegistForm(request.form)
        if form.validate():
            if form.UserPass.data==form.UserPassConfirm.data:
                if request.form.get('checkbox')=="on":
                    #两次密码一致,且同意条款
                    User(username=form.UserName.data,password=form.UserPass.data,email=form.UserMail.data).save()
                    flash(u'注册成功')

                else:
                    flash(u'请阅读并同意服务条款')
            else:
                flash(u'请确认两次密码一致')

            return render_template("signup.html",form=form)

        else:
            if form.errors:
                for error in form.errors.values():
                    flash(error[0])

            return render_template("signup.html",form=form)