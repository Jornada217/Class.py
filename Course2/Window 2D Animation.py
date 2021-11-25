from tkinter import *
import time

#constant is a variable you don't want to change in time. Conventionally in UPPERCASE, but not necessarily.
WIDTH = 650
HEIGHT = 487
xVelocity = 4
yVelocity = 4

window = Tk()
canvas = Canvas(window,width=WIDTH, height=HEIGHT)
canvas.pack()
background_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\background.png")
background = canvas.create_image(0,0,image=background_image,anchor=NW)
pizza_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\Pizza.png")
pizza = canvas.create_image(0,0,image=pizza_image,anchor=NW)
pizza_width = pizza_image.width()
pizza_height = pizza_image.height()


while True:
    coordinates = canvas.coords(pizza)  #Get the coordinates of where the image is located.
    print(coordinates)  #for learning purposes
    if (coordinates[0]>=(WIDTH-pizza_width) or coordinates[0]<0):  #bouncing function. Element [0] is coordinate X
        xVelocity = -xVelocity
    elif (coordinates[1]>=(HEIGHT-pizza_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(pizza, xVelocity, yVelocity)  #This takes 3 arguments
    window.update()  #Update the window for any changes
    time.sleep(0.01)  #Time the thread that will be in charge of running this program will be updating



window.mainloop()