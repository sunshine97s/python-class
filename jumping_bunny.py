import time
from tkinter import *
import winsound

tk = Tk()

canvas = Canvas(tk, width=600, height=600)
my_image1 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bunny1.png')
my_image2 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bunny2.png')
my_image3 = PhotoImage(file='C:\\Users\drago\Documents\python-class\images\\bunny3.png')
tk.image1_id = canvas.create_image(300, 600, anchor="s", image=my_image1)
print(tk.image1_id)
canvas.pack()
def bunnyjump():
    winsound.PlaySound("C:\\Users\drago\Documents\python-class\sounds\jump_sound.wav", winsound.SND_ASYNC)
    btn['state'] = 'disabled'
    second = 0.1
    tk.image2_id = canvas.create_image(300, 300, anchor="center", image=my_image2)
    canvas.delete(tk.image1_id)
    canvas.update()
    time.sleep(second)
    tk.image3_id = canvas.create_image(300, 0, anchor="n", image=my_image3)
    canvas.delete(tk.image2_id)
    canvas.update()
    time.sleep(second*2.5)
    tk.image2_id = canvas.create_image(300, 300, anchor="center", image=my_image2)
    canvas.delete(tk.image3_id)
    canvas.update()
    time.sleep(second)
    canvas.delete(tk.image2_id)
    tk.image1_id = canvas.create_image(300, 600, anchor="s", image=my_image1)
    canvas.update()
    btn.config(state='normal')

btn=Button(tk,text="click to jump", command=bunnyjump)
btn.pack()

tk.mainloop()

