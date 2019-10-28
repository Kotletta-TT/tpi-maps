from app import db
from models import Tpi
from parsertpi import source_pars

tpiData = source_pars()
#print(tpiData)

def addDB(tpiData):
    for i in tpiData:
        rowDB = Tpi(name=i['id'], gpsX=i['gpsX'], gpsY=i['gpsY'], voltage=i['voltage'], timetpi=i['timeTpi'], color=i['color'],status=i['status'])
        db.session.add(rowDB)

    db.session.commit()


def takeDB():
    addDB(tpiData)
    lookAtMe = Tpi.query.order_by(Tpi.id.desc()).limit(14).all()
    return lookAtMe


# addDB(tpiData)
# takeDB()