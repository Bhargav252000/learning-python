from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning Tkinter')

img1 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070232.jpg").resize((400, 400), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070240.jpg").resize((400, 400), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070333.jpg").resize((400, 400), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070358.jpg").resize((400, 400), Image.ANTIALIAS))
img5 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070405.jpg").resize((400, 400), Image.ANTIALIAS))
img6 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070409.jpg").resize((400, 400), Image.ANTIALIAS))
img7 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070452.jpg").resize((400, 400), Image.ANTIALIAS))
img8 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070500.jpg").resize((400, 400), Image.ANTIALIAS))
img9 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_070507.jpg").resize((400, 400), Image.ANTIALIAS))
img10 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_080505.jpg").resize((400, 400), Image.ANTIALIAS))
img11 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_071617.jpg").resize((400, 400), Image.ANTIALIAS))
img12 = ImageTk.PhotoImage(Image.open("image folder/IMG_20191214_071513.jpg").resize((400, 400), Image.ANTIALIAS))

my_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12]

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)


def forward(number):
    global label
    global button_back
    global button_front

    label.grid_forget()
    label = Label(image=my_list[number - 1])

    button_front = Button(root, text=">>", command=lambda: forward(number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(number - 1))

    if number == len(my_list):
        button_front = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_front.grid(row=1, column=2)


def backward(number):
    global label
    global button_back
    global button_front

    label.grid_forget()
    label = Label(image=my_list[number-1])

    button_front = Button(root,text=">>",command=lambda: forward(number+1))
    button_back = Button(root,text="<<",command=lambda: backward(number-1))

    if number == 1:
        button_back = Button(root,text="<<",state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_front.grid(row=1, column=2)


button_back = Button(root, text="<<", command=backward, state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_front = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_front.grid(row=1, column=2)

"""
img = Image.open("bhargav.jpg")
img = img.resize((400,400),Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(img)
my_label = Label(image=my_img)
my_label.pack()
"""

root.mainloop()
