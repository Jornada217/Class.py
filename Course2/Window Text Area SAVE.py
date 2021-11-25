from tkinter import *
from tkinter import filedialog

def submit():
    input_text = text.get("1.0", END)
    print(input_text)

def save():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\joaopaulo\\Google Drive\\Phyton",
                                    defaultextension=".txt",
                                    filetypes=[('Text File', '.txt'), ("Word File", '.doc'),
                                               ("Pdf File", ".pdf"), ("HTML File", ".html"),
                                               ("All files", "*.*")])
    if file is None: #If you close the window or cancel, an ERROR message apears. Solution:
        return
    file_text = str(text.get("1.0", END)) #You can use the console than window to accept a text to be saved
    file.write(file_text)

window = Tk()

save_logo = PhotoImage(file="C:\\Users\\joaopaulo\\Google Drive\\Phyton\\Logos\\save.png")

window.title("Text")
text = Text(window,font=("ink free", 20),
              fg='#6a6e6b',bg='#184022',
            height = 8, width = 20,
            padx=20, pady=20 #Distance text from the border.
            )
text.pack()

button = Button(window, text='Submit', command=submit, bg='#6a6e6b',fg='#184022')
button.pack()

save_button = Button(window, text="Save", command=save,
                     bg='#6a6e6b',fg='#184022',
                     image=save_logo, compound="left")
save_button.pack(side=BOTTOM)

window.mainloop()