from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

brown_dwarfs_url =  'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(brown_dwarfs_url)
print(page)

soup = bs(page.text, 'html.parser')

brown_dwarfs_table = soup.find('table')

temp_list= []
table_rows = brown_dwarfs_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
constellation = []
radius = []
mass = []
distance = []
discovery_year = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    constellation.append(temp_list[i][1])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])
    distance.append(temp_list[i][5])
    discovery_year.append(temp_list[i][9])

df = pd.DataFrame(list(zip(name, constellation, radius, mass, distance, discovery_year)),columns=['Name', 'Constellation', 'Radius', 'Mass', 'Distance', 'Discovery_Year'])
print(df2)

df.to_csv('brown_dwarfs.csv')