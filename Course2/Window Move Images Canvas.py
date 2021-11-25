from tkinter import *

def move_up(event):
    canvas.move(pizza,0,-10)
def move_down(event):
    canvas.move(pizza,0,+10)
def move_right(event):
    canvas.move(pizza,10,0)
def move_left(event):
    canvas.move(pizza,-10,0)

window = Tk()
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
window.bind("<a>", move_left)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)

canvas = Canvas(window, heigh=500, width=500)
pizza_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\Pizza.png")
pizza = canvas.create_image(0,0,image=pizza_image,anchor=NW)
canvas.pack()


window.mainloop()