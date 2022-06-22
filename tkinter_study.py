from tkinter import *
from tkinter import colorchooser

root = Tk()

root['bg'] = '#49d7ff'
root.title('title')
root.wm_attributes('-alpha', 0.7)
root.geometry('600x600')

root.resizable(width=False, height=False)

canvas = Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_line(0,0,500,500)
canvas.create_rectangle(50,100,350,50)
canvas.create_polygon(100, 100, 200, 100, 50, 300)
canvas.create_oval(350, 350, 80,80)
canvas.create_arc(160, 250, 200, 100, extent=180, style=ARC)

canvas.create_rectangle(18, 18, 350, 50, fill='red')
canvas.create_polygon(18, 18, 180, 18, 180, 110, fill='red', outline='black')
canvas.create_oval(18,18, 80, 80, outline='red', fill='green', width=2)
c=colorchooser.askcolor()
canvas.create_rectangle(18, 18, 350, 50, fill=c[1])













root.mainloop()



