import requests 
import lxml
#импортики
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class parser_link():#домен сайт и url
	DOMEN = 'https://ru.redtube.com'
	url = ('https://ru.redtube.com/')
	response = requests.get(url)  #отправляем запрос на сайт для получения html 
	soup = BeautifulSoup(response.text, 'lxml') #преобразуем html для нвшего soup

	def finall_link(soup, DOMEN):
		all_video = soup.find_all('li', class_='js_thumbContainer') #все видосики в блоке
		url1 = soup.find('div', class_='video_title').find('a', class_='js-pop') #углубляемся в блок
		result_url = soup.find('a', class_='js-pop tm_video_title').get('href') #вытаскиавем из полувшиевся тега наш href
		print(result_url)
		url2 = DOMEN + result_url #слагаем наш результат
		print(url2)

	finall_link(soup, DOMEN)
		



