from tkinter import *

def create_window():
    #new_window = Toplevel() #Toplevel() open a window on the top of other windows,/
                                #linked to previous window. Close main window closes windows on top.

    new_window = Tk()      #Tk() is a new comlete independert window.

    entry_window.destroy() #This will close out previous window.

entry_window = Tk()

Button(entry_window, text="New window", command=create_window).pack()

entry_window.mainloop()