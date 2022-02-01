import requests
from bs4 import BeautifulSoup

response = requests.get('https://gamefaqs.gamespot.com/ps5', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.content, 'html.parser')
print(response)
print(soup.title)
print()
releases = soup.find(string='Upcoming PlayStation 5 Game Releases')
#print(releases)

#Extract NORTH AMERICA
#Find the parents
parents = soup.find(string='North America').find_parents()[1]
#print(parents)

#Extract north american games: Teh <dl> holds <dt> and <dd>s
# nagames = soup.find(string='North America').find_parents()[1]
# for i in nagames.find_all('dl'):
#     #print(i.find('dt').get_text())
#     for games in (i.find_all('dd')):
#         #print(games.get_text())

#Extract JAPAN
#Find the parents
parents = soup.find(string='08/17').find_parent()
print(parents)

#Extract north american games: Teh <dl> holds <dt> and <dd>s
# jgames = soup.find(string='Japan').find_parents()[1]
# for i in jgames.find_all('dl'):
#     print(i.find('dt').get_text())
#     for games in (i.find_all('dd')):
#         #print(' '.join(games.get_text().strip().split()))
#         print(games.get_text().strip().split())
