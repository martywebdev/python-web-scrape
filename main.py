import smtplib
import sqlite3
import ssl
import os
import time

import requests
import selectorlib
from dotenv import load_dotenv

load_dotenv()

URL = 'https://programmer100.pythonanywhere.com/tours'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('data.db')

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value


def store(extracted):
    with open('data.txt', 'a') as f:
        f.write(extracted + '\n')


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    receiver = os.getenv('EMAIL')
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def read(extracted):
    parts = [p.strip() for p in extracted.split(",")]
    band, city, date = parts
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()

    return rows
        

if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract(scraped)
    
    if extracted != "No upcoming tours":

        

        row = read(extracted)

        if len(row) == 0 :

            cursor = connection.cursor()
            print(row)
            
            data = tuple(p.strip() for p in extracted.split(","))
            cursor.execute("INSERT INTO events VALUES (?, ?, ?)", data)
            connection.commit()
            connection.close()
            send_email(extracted)
            print('success')
    else: 
        print('try again')
