#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET'])
def index():
    return render_template("login.html")

