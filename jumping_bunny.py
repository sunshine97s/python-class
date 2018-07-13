from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=600, height=600)
my_image = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bunny1.png')
my_image2 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bunny2.png')
my_image3 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bunny3.png')
canvas.create_image(300, 600, anchor="s", image=my_image)
canvas.pack()
def bunnyjump():
    print('button clicked')
    canvas.create_image(300, 300, anchor="center", image=my_image2)
    canvas.create_image(300, 0, anchor="n", image=my_image3)
btn=Button(tk,text="click to jump", command=bunnyjump)
btn.pack()

tk.mainloop()

