import time
from tkinter import *

tk = Tk()
my_image1 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bitcoin1.png')
my_image2 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bitcoin2.png')
my_image3 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bitcoin3.png')
my_image4 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bitcoin4.png')
my_image5 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bitcoin5.png')
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=my_image1)
canvas.create_image(200, 0, anchor="nw", image=my_image3)
canvas.create_image(400, 0, anchor="nw", image=my_image5)
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 50)
canvas.create_polygon(50, 50, 200, 50, 200, 110, fill="", outline="red")
canvas.create_text(150, 150, text='He said, It is Sunday', font=('Times', 24), fill='green')

handle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.create_image(100, 0, anchor="nw", image=my_image2)
canvas.create_image(300, 0, anchor="nw", image=my_image4)
for x in range(0, 100):
    canvas.move(handle, 5, 0)
    tk.update()
    time.sleep(0.05)


def movetriangle(event):
    canvas.move(handle, 5, 0)


canvas.bind_all('<KeyPress-Return>', movetriangle)
tk.mainloop()
