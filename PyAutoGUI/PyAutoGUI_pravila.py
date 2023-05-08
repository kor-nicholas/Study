import pyautogui as pg 
from time import sleep

# Узнавание координат
sleep(2) # задержка кода на 2 секундны
print(pg.size() ) # Рабочий стол
print(pg.position() ) # Курсор 

# Мишка
pg.moveTo(200, 200, 1) # Перемещение курсора на точку плавно
pg.dragTo(200, 200, 1) # Тянет с зажатием

pg.dragRel(300, 300, 1) # Добавляе к DragTo
pg.moveRel(300, 300, 1) # Добавляет к MoveTo

# Клики

sleep(2)
pg.click(clicks= 3, interval = 0.5, button = "left" ) # 3 клика Левой кнопкой с интервалом 0.5 с

pg.doubleClick(clicks = 3, interval = 0.5, button = "right") # Двойной клик,с теми же параметрами

pg.tripleClick(clicks = 3, interval = 0.5, button = "left") # Тройной клик,с теми же параметрами

pg.click( 200, 350 ) # Клик по координатам 

# Скролл

pg.scroll(10) # 10 скроллов вверх (пипец каких маленьких)
pg.scroll(-10) # 10 скроллов вниз (пипец каких больших)

#  Печатать с клавы

pg.press("f") # Только одна клавиша
pg.typewrite(" Hello World", 0.3) # Слово через секунды

# Зажимание сочетания клавиш
 
pg.keyDown("ctrl") # Зажать клавишу
pg.keyDown("f4") # Зажать клавишу

pg.keyUp("ctrl") # Отпустить клавишу
pg.keyUp("f4") # Отпустить клавишу

pg.hotkey("ctrl", "f4") # Просто нажимает и отпускает (+ не нужно в разные строки)

# Самое важное 

pg.click(200, 400, clicks = 5, interval = 0.2, button = "left") # 5 кликов по координатам левой кнопкой

pg.typewrite("Слова которые нужно напечатать", 0.3) # Печатать текст

pg.hotkey("alt", "f4") # Alt + F4