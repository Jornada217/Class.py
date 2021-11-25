from tkinter import *

window = Tk()

canvas = Canvas(window, heigh=500, width=500)
canvas.create_line(0,0,500,500,fill="blue", width=5)
canvas.create_line(0,100,300,500,fill="red", width=10)
canvas.create_rectangle(50,50,250,250,fill='purple')
canvas.create_polygon(50,400,250,400,150,50,fill='green',outline="black", width=5)
points = [400,50,400,250,50,150]
canvas.create_polygon(points)
canvas.create_arc(0,0,500,500,style=ARC)  #You can choose from many styles
canvas.create_arc(0,0,500,500,style=PIESLICE, start=270, extent=45) #start and extent of central angle
canvas.pack()

window.mainloop()