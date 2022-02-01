import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.marketwatch.com/', headers={'USer-Agent': 'Mozilla/5.0'})

print(page)
print()
soup = BeautifulSoup(page.content, 'html.parser')

#Find sections by tag.
all_p = soup.select('p')
#print(all_p)
all_div = soup.select('div')[0]
#print(all_div)

tag_tag = soup.select("div p") #All instances of a tag within a tag, parent first.
#print(tag_tag)
pa = soup.select('div,a') #Multiple tags, all instances of both, separately.
#print(pa)

#Finding sections by CLASS. CSS selectors use a "." before the class name.
article = soup.select('.article__content') #Finds all classes with this name.
#print(article)
#Wherever there is a space in a class name, you need to replace it with a period.
class_element = "element element--section-footer"
element = soup.select('.element.element--section-footer')
#print(element)

#Finding sections with TAG names and CLASS names.
class_btn = 'btn btn--section'
element = soup.select('a.btn.btn--section')
#print(element)

#Using IDs with TAGS. Hash mark (#) represents an ID.
url = 'https://docs.python-requests.org/en/master/user/advanced/#advanced'
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print(page)
soup = BeautifulSoup(page.content, 'html.parser')

#<div class="section" id="advanced-usage">
adv = soup.select('div#advanced-usage')
#print(adv)
id1 = soup.select('span#id1')
#print(id1)

#Extensive list of CSS Selectors:
#https://www.w3schools.com/cssref/css_selectors.asp
