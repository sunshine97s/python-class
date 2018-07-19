from tkinter import *
import time
from tkinter import Canvas

tk = Tk()
canvas: Canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

ball_id = canvas.create_oval(10, 10, 25, 25, fill='white', outline='red')
bar_id = canvas.create_rectangle(0, 390, 100, 400, fill='green', outline='green')

y_delta_step = 1

while 1:
    canvas.move(ball_id, 0, y_delta_step)

    pos = canvas.coords(ball_id)
    if pos[1] <= 0 :
        y_delta_step = 1
    if pos[3] >= 390 :
        y_delta_step = -1

    tk.update()
    time.sleep(.003)
def turn_left(event):
    global x
    x = -2
def turn_right(event):
    global x
    x = 2
canvas.bind_all('<KeyPress-Left>', turn_left)
canvas.bind_all('<KeyPress-Right>', turn_right)
delta_y = -1
while 1:
    canvas.move(bar_id, x, 0)
    canvas.move(ball_id, 0, delta_y)
    pos = canvas.coords(ball_id)
    if (pos[1]) <=0 :
        delta_y = -1
    bar_pos = canvas.coords(bar_id)
    if bar_pos[0] <= 0:
        x = 0
    if bar_pos[2] >=500:
        x = 0
    tk.update_idletasks()
    tk.update()
    time.sleep(.02)
       
tk.mainloop()



        


