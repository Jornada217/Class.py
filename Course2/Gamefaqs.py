import requests
from bs4 import BeautifulSoup

response = requests.get('https://gamefaqs.gamespot.com/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.content, 'html.parser')
print(response)
print(soup.title)
print()

text = soup.get_text(strip=True) #strip gets rid of new lines
#print(text)

#Find all the strings called 'VIta'.
vita_str = soup.find_all(string = 'Vita')
print(vita_str)
print(type(vita_str)) #it is a Result Set
print()

#Find the section Vita belongs to.
vita0 = soup.find_all(string = 'Vita')[0]
print(vita0 + ' ' + '(This is index zero of Vita -> soup.find_all(string = Vita)[0])')
print()

vita_prts = soup.find_all(string = 'Vita')[0].find_parents()
#print(vita_prts)

#Get the link (href) to Vita, add to response and access Vita page.
vita_href = soup.find_all('a', string='Vita')
print(vita_href)
vita_href = soup.find_all('a', string='Vita')[0].get('href')
print(vita_href)
response = requests.get('https://gamefaqs.gamespot.com/vita', headers={'User-Agent': 'Mozilla/5.0'})
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.get_text(strip=True))
top10 = soup.find_all(string = 'Top 10 Games')[0].find_parents()
#print(top10)
#Sliced the parent's list in indexes 0, 1, 2 to find the content of games list:
top10 = soup.find_all(string = 'Top 10 Games')[0].find_parents()[2]
#print(top10)

# ranking = top10.find('ol').find_all('li')[1].get_text()
# print()
# print(ranking)

# Find the ListItems (li), which are inside OrderedLists (ol). For loop:
for i in top10.find_all('ol'):
    for j in top10.find_all('li'):
        #strip will remove spaces, and split will make a list,
        # and join willjoin the lists:
        print(' '.join(j.find('a').get_text().strip().split()))

