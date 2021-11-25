from tkinter import *

def submit():
    print("The temperature is {} Celsius".format(scale.get()))

window = Tk()

hot_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\Logos\\fire.png")
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(window, from_=100, to=0, #make sure from has underline.
              length=300, orient=VERTICAL,
              tickinterval = 10,
              font=("arial", 12),
              troughcolor = "#6a6e6b", fg="green", bg="#a8a59d"
              )
scale.set("15") #sets current value of the slider
scale.pack()

cold_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\Logos\\snow.png")
cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window, text="submit", command=submit)
button.pack(side=BOTTOM)

window.mainloop()