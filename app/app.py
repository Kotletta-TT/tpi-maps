## -*- coding: utf-8 -*-
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'