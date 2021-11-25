from tkinter import *

window = Tk()

frame = Frame(window, bg="pink", bd=5, relief=RAISED,
              padx=20, pady=10,) #instead of adding the button to the window, add to a FRAME
frame.pack(side=LEFT)  #Somehow this pack() cannot be shortcutted to the same line on frame object.
button = Button(frame, text="W", font=("Consolas",25), width=3).pack(side=TOP) #add .pack() to the end! Shortcut
Button(frame, text="A", font=("Consolas",25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas",25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas",25), width=3).pack(side=LEFT)


window.mainloop()