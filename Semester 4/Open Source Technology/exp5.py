
import tkinter
from tkinter import *
from tkinter import messagebox, Label, Entry, Radiobutton, Checkbutton


MainWindow = tkinter.Tk()
MainWindow.title("GUI IN PYTHON")

l1 = Label(MainWindow, text='Name').grid(row=0)
e1 = Entry(MainWindow)
l2 = Label(MainWindow, text="Address").grid(row=1)
e2 = Entry(MainWindow)

l3 = Label(MainWindow, text="Contact No:").grid(row=2)
e3 = Entry(MainWindow)

l4 = Label(MainWindow, text='Gender').grid(row=3)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

rb1 = Radiobutton(MainWindow, text="Male", value=1).grid(row=3, column=1)
rb2 = Radiobutton(MainWindow, text="Female", value=2).grid(row=3, column=2)

var1 = IntVar()
Checkbutton(MainWindow, text='SSC', variable=var1).grid(row=6, sticky=W)
var2 = IntVar()
Checkbutton(MainWindow, text='Diploma in Computer Engineering', variable=var2).grid(row=7, sticky=W)
var3 = IntVar()
Checkbutton(MainWindow, text='HSC', variable=var3).grid(row=8, sticky=W)

text = f''' Welcome {e1.get()}
Your address: {e2.get()}
Contact no. {e3.get()}'''


def Displaywindow():
    messagebox.showinfo(" Yello ", text)


def ask():
    messagebox.askokcancel("Confirm", "The application will be closed")
    MainWindow.destroy()


tkinter.Button(MainWindow, text="Click", width=17, command=Displaywindow).grid(row=9, column=0)
tkinter.Button(MainWindow, text="Close", width=10, command=ask).grid(row=9, column=2)

MainWindow.mainloop()
