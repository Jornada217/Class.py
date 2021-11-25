from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-5)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+5)
def move_right(event):
    label.place(x=label.winfo_x()+5, y=label.winfo_y())
def move_left(event):
    label.place(x=label.winfo_x()-5, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
window.bind("<a>", move_left)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)

pizza_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\Pizza.png")
label = Label(window, image=pizza_image)
label.place(x=0,y=50)


window.mainloop()