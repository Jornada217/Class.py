import requests
import webbrowser
from bs4 import BeautifulSoup

url = 'http://www.marketwatch.com'
response = requests.get(url)  # Response holds the request that you get from the URL
#page = requests.get('http://www.marketwatch.com', headers={'User-Agent': 'Mozilla/5.0'})

#print(response)

soup = BeautifulSoup(response.content, 'html.parser') #two different parameters within BS: content that holds all html /
    #content, and the second one is a parser. There are != parsers available, and html is the default

#(Element we are looking for [div, href, p, table...], attribute)
#find = soup.find_all('div', class_= "element element--latestNews")

#LISTS
#find = soup.find_all('ul', class_ = 'list list--menu j-list')
find = soup.find_all('ul')[0]
print(find)

