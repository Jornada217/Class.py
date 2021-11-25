from tkinter import *

def display():
    if(x.get() == 1):
        print("You agree!")
    else:
        print("You disagree!")

window = Tk()

x = IntVar()

check_logo = PhotoImage(file='C:\\Users\\joaopaulo\\Google Drive\\'
                        'HANASSON LIMITED\\Marketing\\Presentation\\Images\\HOUSE.png')

check_button = Checkbutton(window, text="Check here to agree!", font=("Arial", 15),
                           variable=x,
                           fg='black',bg='#6a6e6b',
                           relief=RAISED, bd=5,
                           padx=5, pady=20,
                           activeforeground='black', activebackground='#6a6e6b',
                           onvalue=1, offvalue=0,
                           command=display,
                           image=check_logo, compound="left")
check_button.pack(side=RIGHT)

window.mainloop()