from tkinter import *

def button1action():
    tk.img = canvas.create_image(0, 0, anchor="nw", image=my_image)


def button2action():
    canvas.delete(tk, tk.img)

tk = Tk()
my_image = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bitcoin.png')
btn1 = Button(tk, text="click me to show picture", command=button1action)
btn1.pack(side=TOP)
btn2 = Button(tk, text="click me to delete picture", command=button2action)
btn2.pack(side=TOP)
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()
tk.mainloop()
