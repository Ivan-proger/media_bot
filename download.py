import youtube_dl
import os

#url_media = 'https://vk.com/video?q=%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D0%BA%D0%BE%D0%B5&z=video-183488070_456246541'

class Download:
	def __init__(self):
		self.res = 0

	def dir0():
		try:
			my_dir = os.getcwd()
			j0in = os.path.join(my_dir, 'media')
			os.chdir(j0in)
		except FileNotFoundError:
			pass

	def inf0 (self, url):
		with youtube_dl.YoutubeDL() as ydl:
			result = ydl.extract_info(url, download=False)
			self.res = result['id']	

		return self.res

	def video_download(self, url, name):
		ydl = youtube_dl.YoutubeDL({'outtmpl': name + '.mp4'})
		with ydl:
		    result = ydl.download([url])



