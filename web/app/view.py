#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template

view = Blueprint('view', __name__)


@view.route('/', methods=['GET'])
def index():
    return render_template("index.html")

