import smtplib
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


def read():
    with open('data.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':

    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read()
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(extracted)
        time.sleep(2)
