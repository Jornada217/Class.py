from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = \
        filedialog.askopenfilename(initialdir="C:\\Users\\joaopaulo\\Google Drive\\Phyton",
                                   title="OPEN THE FILE",
                                   filetypes= (("text files", "*.txt"),
                                   ("all files", "*.*"))) #this will return a string of the file path,
                                                            # you need to read the content.
    file = open(filepath, 'r')
    print(file.read())
    file.close() #Always close the file


window = Tk()

button = Button(text="Open file", command=open_file)
button.pack()

window.mainloop()