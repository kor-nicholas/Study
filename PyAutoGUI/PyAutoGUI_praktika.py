import pyautogui as pg
from time import sleep

pg.click(843,726)

for i in range(10000):
	print(str(i) + ". заход")
	pg.scroll(-1000000000)