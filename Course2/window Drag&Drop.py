from tkinter import *

def drag_start(event):
    widget = event.widget     # This applies the drag&drop to all widgets.
    widget.startx = event.x   #This is where you click on the label, not on the window.
    widget.starty = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startx + event.x
    #label.winfo_x picks the top X coordinate of our lable in the window that we are in
    #label.start.x is the place we clicked in the label itself
    #event.x is where we begin dragging the label
    y = widget.winfo_y() - widget.starty + event.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)
label.bind("<Button-1>", drag_start)  #remeber, bind is bind(event, function)
label.bind("<B1-Motion>", drag_motion)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)


window.mainloop()