from tkinter import *
from tkinter import ttk  #notebook widget is in a separate module inside tkinter

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of frames to windows/displays

tab1 = Frame(notebook) #Object with new frame for tab1, (notebook) ads notebook to the window.
tab2 = Frame(notebook) #Object with new frame for tab2

notebook.add(tab1, text="Tab 1")  #adds the new frames have to be added to the widget, to the collection of displays.
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")   #expand= expand to fill any space otherwise not used.
                                          #fill = fill space on x and y axis.

Label(tab1, text="This is Tab1", width=50, height=25).pack()   #is it here to format?
Label(tab2, text="This is Tab2", width=50, height=25).pack()

window.mainloop()

