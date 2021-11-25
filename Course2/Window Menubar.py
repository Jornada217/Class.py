from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\joaopaulo\\Google Drive\\Phyton",
                                          title = "Open file",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*"))
                                          )
    file = open(filepath, "r")
    print(file.read())
    file.close()

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\joaopaulo\\Google Drive\\Phyton",
                                          title = "Save file",
                                    filetypes=[('Text File', '.txt'), ("Word File", '.doc'),
                                               ("Pdf File", ".pdf"), ("HTML File", ".html"),
                                               ("All files", "*.*")]
                                    )
def cut():
    print('you cut')
def copy():
    print('you copied')
def paste():
    print('you pasted')

window = Tk()

file_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\file.png")
save_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\save.png")
exit_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\exit.png")

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0, font=('MV Boli', 10))  #Tearof is the default dashed line, good to remove.
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open",command=open_file, image=file_logo, compound="left")
filemenu.add_command(label="Save",command=save_file, image=save_logo, compound="left")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit, image=exit_logo, compound='left')

editmenu = Menu(menubar, tearoff=0, font=('MV Boli', 12)) #Tearof is the default dashed line, good to remove.
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)

window.mainloop()