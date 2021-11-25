from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Error: Division by Zero")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text= ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas", 20),
              bg="white", width=24, height=2).pack()


frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(1)).grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35, command= lambda: button_press(2)).grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35, command= lambda: button_press(3)).grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35, command= lambda: button_press(4)).grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35, command= lambda: button_press(5)).grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: button_press(6)).grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35, command= lambda: button_press(7)).grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35, command= lambda: button_press(8)).grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35, command= lambda: button_press(9)).grid(row=2, column=2)
button10 = Button(frame, text=0, height=4, width=9, font=35, command= lambda: button_press(0)).grid(row=3, column=0)
decimal = Button(frame, text=".", height=4, width=9, font=35, command= lambda: button_press(".")).grid(row=3, column=1)
plus = Button(frame, text="+", height=4, width=9, font=35,  bg="#9bbaab",
              command= lambda: button_press("+")).grid(row=0, column=3)
minus = Button(frame, text="-", height=4, width=9, font=35,  bg="#9bbaab",
               command= lambda: button_press("-")).grid(row=1, column=3)
multiply = Button(frame, text="X", height=4, width=9, font=35,  bg="#9bbaab",
               command= lambda: button_press("*")).grid(row=2, column=3)
division = Button(frame, text="/", height=4, width=9, font=35, bg="#9bbaab",
                  command= lambda: button_press("/")).grid(row=3, column=3)
equal = Button(frame, text="=", height=4, width=9, font=35, bg="#5df542",
               command= equals).grid(row=3, column=2)
clear = Button(window, text="clear", height=3, width=12, font=35, bg="#a0a8a4",
               command= clear).pack()

window.mainloop()