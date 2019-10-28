## -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

URL = 'http://172.16.160.53:8020/modem/status.jsp?id=RU0'
URL_STATUS = 'http://172.16.160.53:8020/modem/index.jsp'
WORK_TPI = [41, 42, 43, 44, 45, 47, 48, 50, 52, 53, 55, 56, 57, 58]


def check_online(url = URL_STATUS):

    reqOnline = requests.get(url)
    onlSoup = BeautifulSoup(reqOnline.content, 'lxml')

    result = [{"id": tr.contents[1].get_text().split(' ')[1], "status": tr.contents[5].get_text()} for tr in onlSoup.find_all("tr")[1:]]
    return result


def source_pars(url=URL):
    tuplTpi = []

    for id in WORK_TPI:

        request = requests.get(url+str(id))
        soup = BeautifulSoup(request.content, 'lxml')
        get_xemel = soup.find('pre').get_text()

        xemel = BeautifulSoup(get_xemel, 'lxml-xml')
        id = xemel.id.get_text()
        voltage = float(xemel.voltage.get_text()) / 1000
        x = float(xemel.gpsposition.y.get_text())
        y = float(xemel.gpsposition.x.get_text())

        imgTpi = soup.img['src']
        urlImgTpi = 'http://172.16.160.53:8020' + str(imgTpi).replace('.','')
        timeTpi = soup.find_all('td')[1].get_text()
        a = timeTpi.split(' ')[0]
        convertToTime = datetime.strptime(a, "%Y-%m-%d")
        if datetime.today() - timedelta(days=3) >= convertToTime:
            color = 'black'
        elif voltage < 24.0:
            color = 'yellow'
        else:
            color = 'green'

        TpiInf = {'id': id,
                   'voltage': voltage,
                   'timeTpi': timeTpi,
                   'gpsX': x,
                   'gpsY': y,
                   'color': color,
                   'image': urlImgTpi}
        tuplTpi.append(TpiInf)

    statusTpi = check_online()

    for i in tuplTpi:
        id = i['id']
        for j in statusTpi:
            if j['id'] == id:
                tuplTpi[tuplTpi.index(i)]['status'] = statusTpi[statusTpi.index(j)]['status']


    return tuplTpi


#if __name__ == '__main__':
    #source_pars(url)
    #check_online(url_online)