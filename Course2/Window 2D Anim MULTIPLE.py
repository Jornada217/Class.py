from tkinter import *
from Window_2D_anim_Classes import *
import time

WIDTH = 650
HEIGHT = 433


window = Tk()
canvas = Canvas(window,width=WIDTH, height=HEIGHT)
canvas.pack()
background_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\background2.png")
background = canvas.create_image(0,0,image=background_image,anchor=NW)

volley_ball = Ball(canvas,0,0,100,3,3,"Blue")
golf_ball = Ball(canvas,0,0,20,7,7,"White")
basket_ball = Ball(canvas,0,0,200,1,1,"Red")

pizza_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\Pizza.png")
pizza_width = pizza_image.width()
pizza_height = pizza_image.height()
pizza = Object(canvas, 100, 100, pizza_image, NW, pizza_width, pizza_height, 2, 2)

fire_image = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\fire.png")
fire_width = fire_image.width()
fire_height = fire_image.height()
fire = Object(canvas, 0, 0, fire_image, NW, fire_width, fire_height, 8, 8)


while True:
    volley_ball.move()
    golf_ball.move()
    basket_ball.move()
    pizza.move()
    fire.move()
    window.update()
    time.sleep(0.01)


window.mainloop()