import requests
from time import sleep
from random import randint

def download_video(url):
	with requests.get(url, stream = True) as responce: 
		with open(url.split('/')[-1], 'wb') as file:
			for chunk in responce.iter_content(chunk_size = 16*1024):
				file.write(chunk)

# url = 'https://vss1.coursehunter.net/s/c75c17097781502f6ae7107b101d5468/udemy-angular4/lesson2.mp4'
# print(url.split('/')[-1])

for i in range(3, 421):
	download_video(f'https://vss1.coursehunter.net/s/c75c17097781502f6ae7107b101d5468/udemy-angular4/lesson{i}.mp4')
	print(f'{i} video downloaded')
	sleep(randint(0, 10))

# download_video(f'https://vss1.coursehunter.net/s/c75c17097781502f6ae7107b101d5468/udemy-angular4/lesson1.mp4')

