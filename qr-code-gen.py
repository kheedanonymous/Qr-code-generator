import os
import requests
import bs4
import qrcode
from tkinter import *
from tkinter import ttk

print("*************************\nEnter name with quotation marks\n*************************\n\n")


file = input("Enter name to be encoded: ")

def gen():
	img = qrcode.make(file)

	img.save("qr,png")

	img.show("qr.png")


root = Tk()
root.title("QR CODE GEN")
root.geometry('300x300')


button = Button(root, text="GENERATE", bg="silver", fg="black", command=gen)
button.place(x=100, y=100)

root.mainloop()