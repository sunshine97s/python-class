# Try displaying a photo of yourself  or something else on the canvas using tkinter.
# Make sure it’s a GIF/PNG image! Can you make it move across the screen?
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=1000)
my_image = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bunny.gif')
canvas.create_image(0, 0, anchor="nw", image=my_image)
canvas.pack()
tk.mainloop()


