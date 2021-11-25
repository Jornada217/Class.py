
from tkinter import *

#tkinter is the Phyton's standard GUI, binding to the Tk GUI toolkit
#GUI - Graphical User Interface
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a cotainer to hold these widgets.


window = Tk() #instantiate an instance ofa window.
window.geometry("920x920")
window.title('Joao Window')
#icon = PhotoImage(file="Hanasson Logo Transparente 1.png")
#window.iconphoto(True,icon)
#google HEX colour picker, make sure you have hashtag
count = 0
def click():
    global count
    count += 1
    print("Thanks for clicking {} times.".format(count))

window.config(background="#184022")

#INSERT IMAGE (Going to the label)
photo = PhotoImage(file='C:\\Users\\joaopaulo\\Google Drive\\'
                        'HANASSON LIMITED\\Marketing\\Presentation\\Images\\Brazil.png')

button_logo = PhotoImage(file='C:\\Users\\joaopaulo\\Google Drive\\'
                        'HANASSON LIMITED\\Marketing\\Presentation\\Images\\HOUSE.png')

#labels = is an area widget that holds text and/or an image within a window.
#STEP 1: master of the lable to be in that window.
label = Label(window,
              text="Hello Joao Paulo\n Good Morning",
              font=('arial',20,'bold'),
              fg='#6a6e6b',bg='#184022',
              relief=RAISED, bd=10,
              padx=20, pady=10,
              image=photo, compound="bottom")
label.pack() #STEP 2: Sends the label to the window on top position.
#label.place(x=0, y=0)  #STEP 2: Sends the label to the window on coordinates in pixels.

button = Button(window, text="Click me", font=('Comic Sans', 10, 'bold'),
                fg='#6a6e6b',bg='#184022',
                padx=5, pady=5, activeforeground='#6a6e6b', activebackground='#60a672',
                command=click,
                state=ACTIVE, image=button_logo, compound="bottom")
button.place(x=200, y=320)

window.mainloop() #place window on computer screen, listen for events

#labels
