
from bs4 import BeautifulSoup
import requests
import csv


def extragere():
    agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    url = f'https://www.storia.ro/ro/cautare/inchiriere/apartament/cluj?distanceRadius=0&page=1&limit=36&market=ALL&locations=%5B20000000033%5D&viewType=listing&lang=ro&searchingCriteria=inchiriere&searchingCriteria=apartament&searchingCriteria=locatii-multiple'
    req = requests.get(url, agent)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup


print("a citit url-ul")

soup = extragere()

numefisier = "date.csv"
coloane = ["titlu", 'zona', 'pret']
print("a trecut de fiesier")
with open(numefisier, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(coloane)
    divs = soup.find_all('li', class_='css-p74l73 es62z2j17')
    print("a inceput sa scrie csv")
    for item in divs:
        print("itereaza")
        titlu = item.find(
            'h3', class_='css-1rhznz4 es62z2j11').text.strip()
        print("titlu", titlu)
        zona = item.find(
            'span', class_='css-17o293g es62z2j9').text.strip()
        print("zona", zona)
        pret = item.find(
            'span', class_='css-rmqm02 eclomwz0').text.strip()
        print("pret", pret)

        csvwriter.writerow([titlu, zona, pret])
