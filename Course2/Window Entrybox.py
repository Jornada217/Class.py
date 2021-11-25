from tkinter import *

#Entry widget = textbox that acepts a single line of user input.

def submit():
    username = entry.get() #store the value of the entry box.
    print("Your password is {}!".format(username))
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,font=("arial", 12),
              fg="green", bg="black",
              show="*")
entry.insert(0,"Insert your password:")
entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()