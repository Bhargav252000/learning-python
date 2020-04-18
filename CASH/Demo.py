"""
## ADDING BUTTON ON THE FRAME USING TKINTER
from tkinter import *

root = Tk()

newFrame = Frame(root)
newFrame.pack()

newFrame2 = Frame(root)
newFrame2.pack(side=BOTTOM)

button1 = Button(newFrame,text="EXPLORE SPACE",fg="Blue")
button2 = Button(newFrame2,text="EXPLORE ONLY MARS",fg="Black")

button1.pack()
button2.pack()
root.mainloop()

"""
"""
## ADDING BUTTONS AND LABELS TO GIVEN GRIDS 

from tkinter import *

root = Tk()
label1 = Label(root, text="Firstname")
label2 = Label(root, text="Lastname")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row =0, column =0)
label2.grid(row =1, column =0)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

button1 = Button(root,text="SUBMIT",fg="black")

button1.grid(row=3,column=1)

root.mainloop()
"""

"""
### SELF-ADJUSTING WIDGETS 
from tkinter import*

root = Tk()

label1 = Label(root,text="First", bg= "Black",fg="White")
label1.pack(fill=X)

label2 = Label(root,text="Second", bg= "Red",fg="White")
label2.pack(side=LEFT, fill=Y)


root.mainloop()
"""

"""
### User-Interface Widgets

from tkinter import *

class ButtonClick:

    def __init__(self, root1):
        frame = Frame(root1)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quit = Button(frame, text="Exit", command=frame.quit)
        self.quit.pack(side=LEFT)

    def printmessage(self):
        print('Button Clicked')


root = Tk()

t = ButtonClick(root)

root.mainloop()

"""

"""
from tkinter import *

def function1():
    print('Menu Item Clicked')

def Exit():
    


root = Tk()

menu = Menu(root)
root.config(menu=menu)

sub1 = Menu(menu)

menu.add_cascade(label="File",menu=sub1)

sub1.add_command(label="Project",command=function1)
sub1.add_command(label="Save",command=function1)
sub1.add_command(label="Exit",command=)
"""

