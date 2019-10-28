## -*- coding: utf-8 -*-
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
db = SQLAlchemy(app)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'