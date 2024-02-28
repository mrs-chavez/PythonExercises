from tkinter import *

count = 0

def button_clicked():
    global count
    count = count + 1
    count_text.config(text=count)


window = Tk()

count_text = Label(text="0")
count_text.pack()

button = Button(text="Click", command=button_clicked)
button.pack()


window.mainloop()
