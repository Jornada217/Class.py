from tkinter import *
from tkinter import messagebox  #imports messagebox library


def click():
    #messagebox.showinfo(title="This is an info message box.",message="You clicked the button, haha!")
    #messagebox.showwarning(title="Warning.", message="WARNING!")
    #messagebox.showerror(title="ERROR", message="FATAL ERROR!")
    # if messagebox.askokcancel(title="OK or CANCEL", message="Do you want to quit?"):
    #     print("You clicked OK")
    # else:
    #     print("You clicked quit")
    # if messagebox.askretrycancel(title="OK or CANCEL", message="Do you want to retry?"):
    #     print("You clicked RETRY")
    # else:
    #     print("You clicked cancel")
    #TO RETURN A BOOLEAN VALUE:
    # if messagebox.askyesno(title="YES/NO", message="Please decide, yes or no?"):
    #     print("You clicked YES")
    # else:
    #     print("You clicked NO")
    #ASKING QUESTION. Will return a boolean on yes or no.
    # answer = messagebox.askquestion(title="Answer the question.", message="Do you want to answer the question?")
    # if (answer == "yes"):
    #     print("You have answered the question")
    # else:
    #     print("You have not answered the question")
    # ASKING YES, NO, CANCEL. results= True, False or None.
    #you can choose the icon to 'error', 'warning', 'info'
    answer = messagebox.askyesnocancel(title="yes/no/cancel", message="Yes, no or cancel?", icon='info')
    if(answer == True):
        print("You chose yes.")
    elif(answer == False):
        print("You chose no.")
    else:
        print("Why are you canceling?")


window = Tk()

button = Button(window, command=click,
                text="Click me!")
button.pack()

window.mainloop()
