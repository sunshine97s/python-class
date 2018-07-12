# Modify the code for the moving triangle to make it move across the screen
# to the right,
# then down,
# then back to the left,
# and then back to its starting position.

from tkinter import *
import time


def leftKeyAction(event):
    print('left key pressed')


tk = Tk()
canvas = Canvas(tk, width=1000, height=500)
canvas.pack()
handle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
tk.bind('<KeyRelease-Left>', leftKeyAction)

for x in range(0, 190):
    canvas.move(handle, 5, 0)
    tk.update()
    time.sleep(0.05)
for x in range(0, 88):
    canvas.move(handle, 0, 5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 190):
    canvas.move(handle, -5, 0)
    tk.update()
    time.sleep(0.05)
for x in range(0, 88):
    canvas.move(handle, 0, -5)
    tk.update()
    time.sleep(0.05)

tk.mainloop()
