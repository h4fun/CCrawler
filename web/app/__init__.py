#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import render_template

from conf.config import config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    """
        register blueprint
    """
    from app.views.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.views.login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    from app.views.signup import signup as signup_blueprint
    app.register_blueprint(signup_blueprint)

    @app.errorhandler(404)
    def error404(e):
        return render_template("error/404.html"), 404

    return app
