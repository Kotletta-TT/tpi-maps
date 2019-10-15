## -*- coding: utf-8 -*-

from app import app
from flask import render_template
from parsertpi import source_pars

@app.route('/')
def index():
    tpiData = source_pars()
    return render_template('index.html', tpiData=tpiData)