## TPI-Maps
#### This project I build for the company Ltd "Start-Sochi", where in I works.

This is web application view-maps(YandexMaps Api 2.1) works led-board information.
   
   
**Algorithm works:**

- Flask start web application
- Run async web-scrapping(HTML+XML) answer led-board
- Added data to DB (PostgreSQL)
- Sorted data in DB and repeat web-scrapping 10 minutes
- Request from user
- Build index.html to template, using DB
- View and enjoy!

**UI:**

- System authorization
- System search
- View information led-board in real time, just click marker.


**Need to install:**

###### This instruction suggests use linux distribution
`PostgreSQL 11`,`Python 3.x`

need dependence to project can take:

`pip install -r requirements.txt`

We need install additional library:

`sudo apt-get install libpq-dev`
`sudo apt-get install python3-dev`
 needed for psycopg2
 
 