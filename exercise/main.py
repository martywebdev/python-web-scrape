import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = 'https://programmer100.pythonanywhere.com/'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

x = soup.find(id='temperatureId').get_text()

with open('data', 'a') as f:
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")

    entry = f'{now}, {x}, \n'
    f.write(entry)
