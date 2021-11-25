from tkinter import *

def do_something(event): #You have to set one parameter for this function, in this case, #event from bind command.
    print("Mouse coordinates: {}, {}".format(str(event.x),str(event.y)))

window = Tk()

#window.bind("<Button-1>", do_something)  #.bind(event, function), Button-3 = Right button
                                         #Button-1 = left button, Button-2 = Press scroll butto
# window.bind("<ButtonRelease>", do_something)  #Command when button is released
# window.bind("<Enter>", do_something) # Point the mouse enter the window
# window.bind("<Enter>", do_something) # Point the mouse enter the window
# window.bind("<Leave>", do_something)  # Point the mouse exits the window
# window.bind("<Motion>", do_something) # Where the mouse moved

window.mainloop()
