import requests
import webbrowser
from bs4 import BeautifulSoup

url = 'http://geoconvert.mimas.ac.uk/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
#find = soup.find_all('div', id='maincontent')
#find= soup.find_all('div', clas_='divRestart')
#print(find)
find = soup.find_all('div', id='form1')
#print(find)

#links: pull specific link
#find = soup.find('a').get('href')
#find = soup.find_all('a')[0].get('href')
#print(find)

#images. Tag is 'img', and 'src' attribute
find = soup.find_all('img', src='images/symbol4.png')
find = soup.find('img').get('src')
print(find)
