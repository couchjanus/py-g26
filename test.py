import requests
import html5lib
from bs4 import BeautifulSoup
import csv

url = 'https://www.python.org/blogs/'

res = requests.get(url)

soup = BeautifulSoup(res.content, 'html5lib')
# print(soup.prettify())

r = soup.find('section', attrs={'class':'main-content'})

# print(r)

news = []

for row in r.findAll('li'):
    n = {}
    n['title'] = row.a.text
    n['url'] = row.a['href']
    if row.time is None:
        n['date'] = 'no date'
    else:
        n['date'] = row.time.text
    
    news.append(n)
fn = 'news.csv'
with open(fn, 'w', newline='') as f:
    w = csv.DictWriter(f, ['title','url','date'])
    w.writeheader()
    for n in news:
        w.writerow(n)
