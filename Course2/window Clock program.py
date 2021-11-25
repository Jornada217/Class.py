from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%d %b - %Y")
    day_label.config(text=day_string)

    week_string = strftime("%A")
    week_label.config(text=week_string)

    window.after(1000, update)   #has two atributes .aflter(time, funtion) upsdate in miliseconds the function you want to call again.

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="green", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25), fg="blue", bg="black")
day_label.pack()

week_label = Label(window, font=("Arial", 20), fg="white", bg="black")
week_label.pack()

update()


window.mainloop()

