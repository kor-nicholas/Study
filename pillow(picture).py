from PIL import Image
from time import sleep

img = Image.open("1.png") # Открыть фото (в коде)
img.show() # Открыть фото (как по двойному щелчку)

# Информация о фото
print(img.size) # размеры (x,y )
print(img.format) # формат фото
print(img.mode) # мод
print(img.histogram) # гистрограма фото

# Сохранение фото
img.thumbnail((200,200)) # копия фото, но в уменьшеном виде
img.save("mini.png") # сохраняем фото

# Обрезка фото (crop - обрезать)
crop_img = img.crop((100,200,300,400)) # 100 и 200 - координаты левого вепхнего угла; 300 и 400 - координаты правого нижнего угла
crop_img.show()