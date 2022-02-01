import requests
from bs4 import BeautifulSoup

url = 'https://www.espn.co.uk/nba/stats/player/_/table/offensive/sort/avgAssists/dir/desc'

headers = {'User-Agent': 'Mozilla/5.0'}
# Headers are a way to imitate browsers. Each browser has an specific browser to communicate with the site.
#www.whoishostingthis.com/tools/user-agent/
response = requests.get(url, headers=headers)
print(response) #make sure that your reponse status is [200], so it means that you are connected to the site.

soup = BeautifulSoup(response.content, 'html.parser')

#'Table Table--align-right Table--fixed Table--fixed-left'
stat_table = soup.find_all('table', class_ ='Table Table--align-right' )
print(len(stat_table))
print(stat_table)
print(type(stat_table)) #find_all returns a Result Set. We need to extract the table to use the data.

stat_table = stat_table[0] #Stat_table will be the 0th element located at this stat_table, the 0th result.
print(stat_table)
print(type(stat_table)) #Now it returns an Element Tag.

#Using for loops to pull out each td (each cell from each line).
for row in stat_table: #pull out all the rows
    r = stat_table.find_all('tr')
    for cell in r:
        c = stat_table.find_all('td')
        print('\n')
        print(cell.text.ljust)

with open('basketball_stats.txt', 'w') as r:
    for row in stat_table:  # pull out all the rows
        rr = stat_table.find_all('tr')
        for cell in rr:
            c = stat_table.find_all('td')
            r.write(cell.text.ljust(50))
            r.write('\n')


