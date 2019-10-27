## -*- coding: utf-8 -*-
import lxml
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time, timedelta

url = 'http://172.16.160.53:8020/modem/status.jsp?id=RU0'
url_online = 'http://172.16.160.53:8020/modem/index.jsp'
work_tpi = [41,42,43,44,45,47,48,50,52,53,55,56,57,58]
currentDate = datetime.today()


def check_online(url_online='http://172.16.160.53:8020/modem/index.jsp'):

    reqOnline = requests.get(url_online)
    onlSoup = BeautifulSoup(reqOnline.content, 'lxml')

    #====== ТРЕТЬЯ Версия =======
    result = [{"id": tr.contents[1].get_text().split(' ')[1], "status": tr.contents[5].get_text()} for tr in onlSoup.find_all("tr")[1:]]
    print(result)

    # ====== ВТОРАЯ Версия ======
    # tuplOnline = []
    #
    # getOnline = onlSoup.find_all('tr')[1:]
    # for tr in getOnline:
    #     tds = tr.find_all('td')
    #
    #     name = tds[0].getText()
    #     status = tds[2].getText()
    #     tuplOnline.append({
    #         'id': name,
    #         'status': status,
    #     })
    # return tuplOnline




    # ===== ПЕРВАЯ Версия =====
    #
    # for i in work_tpi:
    #     ruId.append('RU0' + str(i))
    #
    # for i in getOnline:
    #     if 'Modem' in i.text:
    #         tempId.append(i.text.split(' ')[1])
    #
    # result = list(set(ruId) & set(tempId))
    # print(result)
    #
    #     elif 'ONLINE' in i.text:
    #         status = 'ONLINE'
    #         dictOnl = {'id': tempId,
    #                    'status': status}
    #     elif 'OFFLINE' in i.text:
    #         status = 'OFFLINE'
    #         dictOnl = {'id': tempId,
    #                    'status': status}
    #         tuplOnline.append(dictOnl)
    #         print(tuplOnline)


def source_pars(url='http://172.16.160.53:8020/modem/status.jsp?id=RU0'):
    tuplTpi = []

    for id in work_tpi:

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
        if currentDate - timedelta(days=3) >= convertToTime:
            color = 'red'
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
    print(tuplTpi)

    return tuplTpi

def viewByTime():
    pass


if __name__ == '__main__':
    source_pars(url)
    check_online(url_online)