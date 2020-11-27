from bs4 import BeautifulSoup

import requests 
import lxml


class parser_link():
	def __init__(self):
		self.DOMEN = 'https://www.xvideos.com'
		self.url = ('https://www.xvideos.com/')
		self.response = requests.get(self.url)  #отправляем запрос на сайт для получения html 
		self.soup = BeautifulSoup(self.response.text, 'lxml') #преобразуем html для нвшего soup
		self.result_urls = ['sdsdsds']
		self.result_url0 = self.soup.find('p', class_='title').find('a').get('href') #вытаскиавем из полувшиевся тега наш href

	def finall_link(self):
		self.result_url0 = self.DOMEN + self.result_url0
		#self.result_urls.append(self.result_url0)

		#if self.result_urls[0] != result_url:
			#return result_url





