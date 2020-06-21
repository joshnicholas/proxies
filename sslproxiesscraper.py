from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 

proxy_path = ''
heados = ['IP Address', 'Port', 'Code','Country','Anonymity','Google','Https','Last Checked']

r = requests.get('https://www.sslproxies.org/')
soup = bs(r.text, 'html.parser')
tablo = soup.find(id='proxylisttable')
listo = []
proxies = []
for row in tablo.find_all('tr'):
    row_list = []
    cells = row.find_all('td')
    for cell in cells:
        row_list.append(cell.text)
    listo.append(row_list)

listo_zwei = [x for x in listo if (len(x) > 1)]

df = pd.DataFrame(listo_zwei, columns=heados)

df.to_csv('f{proxy_path}proxies.csv', index=False)

print(df)
