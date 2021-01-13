from bs4 import BeautifulSoup

import requests 


class parser_link():
	def __init__(self):
		self.DOMEN = 'https://www.xxxxxxx.com'
		self.url = ('https://www.xxxxxx.com/')
		self.response = requests.get(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"})  #отправляем запрос на сайт для получения html 
		self.soup = BeautifulSoup(self.response.text) #преобразуем html для нвшего soup
		self.result_urls = ['sdsdsds']
		self.result_url0 = self.soup.find('p', class_='title').find('a').get('href') #вытаскиавем из полувшиевся тега наш href





