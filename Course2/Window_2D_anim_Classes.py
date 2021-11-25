class Ball:  #This class is from 2D animation with multiple objects
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,Colour):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=Colour)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
    def move(self):
        coordinates = self.canvas.coords(self.image) #get the coordinates
        #print(coordinates)  #Educatoinal purposes
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        elif(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)

class Object:
    def __init__(self, canvas, x, y, image, anchor, width, height, xVelocity, yVelocity):
        self.canvas = canvas
        self.image = canvas.create_image(x, y, image=image, anchor=anchor)
        self.width = width
        self.height = height
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)
        if coordinates[0]>=(self.canvas.winfo_width()-self.width) or coordinates[0]<0:
             self.xVelocity = -self.xVelocity
        elif coordinates[1]>=(self.canvas.winfo_height()-self.height) or coordinates[1]<0:
             self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)