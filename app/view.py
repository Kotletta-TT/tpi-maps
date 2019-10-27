## -*- coding: utf-8 -*-

from app import app
from flask import render_template
from parsertpi import source_pars
from dbcapital import takeDB

@app.route('/')
def index():
    tpiData = takeDB()
    return render_template('index.html', tpiData=tpiData)