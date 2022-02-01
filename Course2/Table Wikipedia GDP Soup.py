import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')



stat_table = soup.find_all('table', class_ = 'wikitable sortable static-row-numbers plainrowheaders mw-datatable')
print(type(stat_table))

stat_table = stat_table
print(type(stat_table))

for row in stat_table:
    stat_table.find('tr')
    for cell in stat_table:
        stat_table.find('td')
        print(cell.text)