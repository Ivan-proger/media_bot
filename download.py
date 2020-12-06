import youtube_dl
import os


class Download:
	def __init__(self):
		self.res = 0

	def inf0 (self, url):
		with youtube_dl.YoutubeDL() as ydl:
			result = ydl.extract_info(url, download=False)
			self.res = result['id']	

		return self.res

	def video_download(self, url, name):
		ydl = youtube_dl.YoutubeDL({'outtmpl': name + '.mp4'})
		with ydl:
		    result = ydl.download([url])



