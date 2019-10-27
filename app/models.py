from app import db
from datetime import datetime

class Tpi(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5))
    gpsX = db.Column(db.Float)
    gpsY = db.Column(db.Float)
    voltage = db.Column(db.Float)
    timetpi = db.Column(db.DateTime, default=datetime.now())


    def __init__(self, *args, **kwargs):
        super(Tpi, self).__init__(*args, **kwargs)