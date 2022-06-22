from logging import root
from tkinter import*
from tkinter import ttk
import os
from PIL import Image, ImageTk
import tkinter

root = Tk()
root.title('Chương trình AI phát hiện ung thư da')
root.geometry("640x400")

image1 = Image.open("C:/AICS5/UTDA/logo.png")
test = ImageTk.PhotoImage(image1)
label1 = Label(root, image=test)
label1.place(x=0, y=0)
img = Label(root)
root.iconbitmap('C:/AICS5/UTDA/logo.ico')
img.place(x=0, y=0)

def open():
    root.destroy()
    os.system('python img.py')

bttn1 = Button(text= "Chụp Ảnh" , command=open, pady = 3)
bttn1.pack()
bttn1.place(x=150, y=330)


def open_web():
    root.destroy()
    os.system('py -m streamlit run app.py')


bttn2 = Button(text="Kiểm Tra", command=open_web, pady = 3)
bttn2.pack()
bttn2.place(x=250, y=330)

def close():
    root.destroy()

bttn3 = Button(text="Thoát", command=close, pady = 3)
bttn3.pack()
bttn3.place(x=350   , y=330)

from numpy import void
import pyttsx3




root.mainloop() 