from tkinter import *
from tkinter.ttk import *  #progress bar
import time
#progress bar

def submit():
    tasks = 10
    x = 0
    while(x<tasks):
        time.sleep(.1)
        bar["value"]+=10
        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        window.update_idletasks()


window = Tk()

percent = StringVar()

titlelabel = Label(window, text="Enter your info").grid(row=0, column=0, columnspan=2)

firstname_label = Label(window, text='First name: ').grid(row=1, column=0)
firstname_entry = Entry(window).grid(row=1, column=1)

lastname_label = Label(window, text='Last name: ').grid(row=2, column=0)
lastname_entry = Entry(window).grid(row=2, column=1)

email_label = Label(window, text='Email: ').grid(row=3, column=0)
email_entry = Entry(window).grid(row=3, column=1)

submitbutton = Button(window, text="Submit", command=submit).grid(row=4, column=0, columnspan=2) #Place in between two colums

bar = Progressbar(window,orient=HORIZONTAL, length=300)
bar.grid(row=5, column=0,columnspan=2, pady=10)
bar_progress = Label(window, textvariable=percent)
bar_progress.grid(row=6, column=0,columnspan=2)

window.mainloop()