import qrcode
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x400')
root.title("QR CODE GENERATOR")

def main():
	img = qrcode.make(str(e.get()))

	img.save((f.get()))

	img.show((f.get()))


l1 = Label(root, text="Enter word/sentence to turn to QR code:")
l1.pack()
e = Entry(root, bg="silver", fg="black")
e.pack()
l2 = Label(root, text="Save file as:")
l2.pack()
f = Entry(root, bg="silver", fg="black")
f.pack()
b = ttk.Button(root, text="GENERATE", command = main)
b.pack()

root.mainloop()
