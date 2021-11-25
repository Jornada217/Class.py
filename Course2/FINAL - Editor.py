import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import *

def new_file():
    answer = messagebox.askyesnocancel(title="Quit", message="Do you want to save before quit?", icon='info')
    if (answer == True):
        save_file()
    elif (answer == False):
        window.title("New_file")
        text_area.delete(1.0, END)
    else:
        return

def open_file():
    file = askopenfilename(initialdir="C:\\Users\\joaopaulo\\Google Drive\\Phyton",
                                          title = "Open file",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*"))
                                          )
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except Exception:
        print("Couldn't read file")
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialdir="C:\\Users\\joaopaulo\\Google Drive\\Phyton",
                                          title = "Save file", initialfile='untitled.txt',
                                    defaultextension='.txt',
                                    filetypes=[('Text File', '.txt'), ("Word File", '.doc'),
                                               ("Pdf File", ".pdf"), ("HTML File", ".html"),
                                               ("All files", "*.*")]
                                  )
    if file is None:
        return
    else:
        try:
           window.title(os.path.basename(file))
           file = open(file, "w")
           file.write(text_area.get(1.0, END))
        except Exception:
            print("Couldn't save file.")
        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")
def copy():
    text_area.event_generate("<<Copy>>")
def paste():
    text_area.event_generate("<<Paste>>")

def change_colour():
    color = colorchooser.askcolor(title="Color")   #returns Tupple, and needs to pick RBG or HEX
    text_area.config(fg=color[1])  #HEX

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def about():
    showinfo("About this program", "Version 1.0.0.4.23.444")

def quit():
    answer = messagebox.askyesnocancel(title="Quit", message="Do you want to save before quit?", icon='info')
    if (answer == True):
        save_file()
        window.destroy()
    elif (answer == False):
        window.destroy()
    else:
        return




window = Tk()
window.title("Jota Pad")
file = None
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

new_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\new.png")
file_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\file.png")
save_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\save.png")
exit_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\exit.png")
cut_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\cut.png")
copy_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\copy.png")
paste_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\paste.png")

font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("20")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
window.grid_rowconfigure(0, weight=1)  #This will allow the text area to expand
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
text_area.config(yscrollcommand=scroll_bar.set)   # configure text area with scroll bar

frame = Frame(window)
frame.grid()

colour_button = Button(frame, text="Color", command=change_colour)
colour_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)


menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0, font=('arial', 12)) #Tearof is the default dashed line, good to remove.
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New",command=new_file, image=new_logo, compound="left")
filemenu.add_command(label="Open",command=open_file, image=file_logo, compound="left")
filemenu.add_command(label="Save",command=save_file, image=save_logo, compound="left")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit, image=exit_logo, compound='left')

editmenu = Menu(menubar, tearoff=0, font=('arial', 12))
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=copy, image=copy_logo, compound="left")
editmenu.add_command(label="Cut", command=cut, image=cut_logo, compound="left")
editmenu.add_command(label="Paste", command=paste, image=paste_logo, compound="left")

helpmenu = Menu(menubar, tearoff=0, font=('arial', 12))
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

window.mainloop()