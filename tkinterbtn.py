from tkinter import*
def buttonaction ():
    print('hello world')
    print("This is Chloe")
tk=Tk()
btn=Button(tk,text="click me to print secret word", command=buttonaction)
btn.pack()

tk.mainloop()