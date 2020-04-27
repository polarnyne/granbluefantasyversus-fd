'''Viejo, no entiendo una goma'''
import bs4
import requests
import pandas as pd

response = requests.get("https://www.dustloop.com/wiki/index.php?title=GBVS/Gran/Frame_Data")

soup = bs4.BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class':'wikitable'}).tbody

rows = table.find_all('tr')
columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]

df = pd.DataFrame(columns = columns)

for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(values, index = columns), ignore_index = True)
    print(df)

