import requests 
import lxml

from bs4 import BeautifulSoup
from urllib.parse import urlparse


DOMAIN = 'www.xvideos.com'
HOST = 'http://' + DOMAIN

url = ('https://ru.redtube.com/')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#items = soup.find_all('div', class_='thumb-under')


items = []

for item in items:
	#print('sdsdsdsd')
	items.append({
		'title': item.find('a', class_='js-pop tm_video_title ').get_text()
		})


##print(link['href'])


print(items)
print('')









