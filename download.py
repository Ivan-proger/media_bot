import youtube_dl
import os

url_media = 'https://vk.com/video?q=%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D0%BA%D0%BE%D0%B5&z=video-183488070_456246541'

class Download(url_media):
	def __init__(self):
			self.ydl_opts = {}

	def dir():
		try:
			my_dir = os.getcwd()
			j0in = os.path.join(my_dir, 'media')
			os.chdir(j0in)
		except FileNotFoundError:
			pass

	def video_download(self):
		#скачиваем видео с ресурса
		with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
			return ydl.download([url_media])



