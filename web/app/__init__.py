#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from conf.config import config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    """
        register blueprint
    """
    from view import view as view_blueprint
    app.register_blueprint(view_blueprint)

    return app
