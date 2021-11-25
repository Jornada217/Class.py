from tkinter import *

food = ["Pizza", "Hamburguer", "Hotdog"]

def order():
    if (x.get() == 0):
        print("You chose pizza")
    elif (x.get() == 1):
        print("You chose burguer")
    elif (x.get() == 2):
        print("You chose Hot Dog")
    else:
        print("What? haha")

window = Tk()
window.title('Joao Radio Window')

pizzalogo = PhotoImage(file='BRAVO 1.png')
burguerlogo = PhotoImage(file='BRAVO 2.png')
hotdoglogo = PhotoImage(file='HOUSE.png')
foodImages = [pizzalogo, burguerlogo, hotdoglogo]


x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window, text=food[index], font=("arial", 20),
                               variable=x, #Goups radiobuttons together is they share the same variable
                               value=index, #Assigns each radio button a different value.
                               image=foodImages[index], compound='left', #The image for each index.
                               indicator=0, #removes the indicator and looks like a button. 1 to return on circle.
                               command=order #Will set command of radio button to function. don't use parenthesis.
                               )

    radio_button.pack(anchor=W)

window.mainloop()

