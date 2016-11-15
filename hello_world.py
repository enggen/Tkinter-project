from tkinter import *
from tkinter import ttk

root = Tk()
#1

'''
# root.title = ("First GUI")
#ttk.Button(root, text = "Hellow World").grid()
'''

#2
'''
frame = Frame(root)


labelText = StringVar()

label = Label(frame, textvariable = labelText)
button = Button(frame, text = "Click Me")

labelText.set("I'm a Label")

label.pack()
button.pack()
frame.pack()
'''
#3

'''
frame = Frame(root)

Label(frame, text = "A bunch of Buttons").pack()

Button(frame, text = "B1").pack(side=LEFT, fill=Y)
Button(frame, text = "B2").pack(side=TOP, fill=X)
Button(frame, text = "B3").pack(side=RIGHT, fill=X)
Button(frame, text = "B4").pack(side=LEFT, fill=X)

frame.pack()
'''

#4

'''
Label(root, text = "First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, padx=4)

Label(root, text = "Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, padx=4)

Button(root, text = "Submit").grid(row=3)
'''
#5

'''
Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)
'''
#6

def get_sum(event):
    # Get the value stored in the entries
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 + num2

    # Delete the value in the entry
    sumEntry.delete(0, "end")

    # Insert the sum into the entry
    sumEntry.insert(0, sum)


root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")

# When the left mouse button is clicked call the
# function get_sum
equalButton.bind("<Button-1>", get_sum)

equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()