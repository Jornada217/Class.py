from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print('your order is:')
    for i in food:
        print(i)

def customise():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def remove():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()
window.title("MENU")

listbox = Listbox(window,
                  font=("constantia", 20),
                  bg="#6a6e6b",
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Burguer")
listbox.insert(3, "Hotdog")
listbox.insert(4, "Pasta")
listbox.insert(5, "Icecream")
listbox.config(height=listbox.size()) #this adjusts the size dinamically.

entry_box = Entry(window,
                  font=("arial", 12),
                  fg="green", bg="white",
                  )
entry_box.pack()

customise_button = Button(window, text="Customise Menu", command=customise)
customise_button.pack()

remove_button = Button(window, text="Remove Item", command=remove)
remove_button.pack()

submit_button = Button(window, text="Place Order", command=submit)
submit_button.pack()

window.mainloop()