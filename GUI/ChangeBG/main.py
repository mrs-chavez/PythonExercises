from tkinter import *

count = 0

def change_to_red():
    window.config(background="red")

def change_to_blue():
    window.config(background="blue")

window = Tk()


red_button = Button(text="Red", command=change_to_red)
red_button.pack()

blue_button = Button(text="Blue", command=change_to_blue)
blue_button.pack()


window.mainloop()
