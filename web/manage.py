#!/usr/bin/env python
# coding=utf-8

from flask_script import Manager, Server
from app import create_app
from flask_wtf import CSRFProtect
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
csrf = CSRFProtect()
csrf.init_app(app)


server = Server(host="0.0.0.0", port=5000)
manager.add_command("runserver", server)

if __name__ == "__main__":
    manager.run()
