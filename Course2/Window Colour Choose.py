from tkinter import *
from tkinter import colorchooser  #this is a submodule

def click():
    window.config(bg=colorchooser.askcolor()[1])  #This changes backgound colour. [0]RBG, [1]HEX

window = Tk()
window.title("Color Window")
window.geometry('420x420')

button = Button(text= "Choose the colours", command=click)
button.pack()

window.mainloop()