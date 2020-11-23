import youtube_dl
import os

url_media = 'https://vk.com/video?q=%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D0%BA%D0%BE%D0%B5&z=video-183488070_456246541'

class download(url_media):
	#узнаем текущию дерикторию скрипта
	my_dir = os.getcwd()
	#объединяем тек. директорию и папку проекта
	j0in = os.path.join(my_dir, 'media')
	#переходим по получившиемся директории
	next_dir = os.chdir(j0in)
	ydl_opts = {}
	#скачиваем видео с ресурса
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url_media])




