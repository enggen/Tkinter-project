from tkinter import *
from tkinter import ttk 

#root = Tk()
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

'''
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
'''

import tkinter.filedialog


class TextEditor:
    # Quits the TkInter app when called
    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):

        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                                                      initialdir='/Users/derekbanas/PycharmProjects')

        if txt_file:
            self.text_area.delete(1.0, END)

            # Open file and put text in the text widget
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())

                # Update the text widget
                root.update_idletasks()

    def save_file(self, event=None):

        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            # Get text in the text widget and delete the last newline
            data = self.text_area.get('1.0', END + '-1c')

            # Write the text and close
            file.write(data)
            file.close()

    def __init__(self, root):

        self.text_to_write = ""

        # Define title for the app
        root.title("Text Editor")

        # Defines the width and height of the window
        root.geometry("600x550")

        frame = Frame(root, width=600, height=550)

        # Create the scrollbar
        scrollbar = Scrollbar(frame)

        # yscrollcommand connects the scroll bar to the text
        # area
        self.text_area = Text(frame, width=600, height=550,
                              yscrollcommand=scrollbar.set,
                              padx=10, pady=10)

        # Call yview when the scrollbar is moved
        scrollbar.config(command=self.text_area.yview)

        # Put scroll bar on the right and fill in the Y direction
        scrollbar.pack(side="right", fill="y")

        # Pack on the left and fill available space
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()

        # Create the menu object
        the_menu = Menu(root)

        # Create a pull down menu that can't be removed
        file_menu = Menu(the_menu, tearoff=0)

        # Add items to the menu that show when clicked
        # compound allows you to add an image
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

        # Add a horizontal bar to group similar commands
        file_menu.add_separator()

        # Call for the function to execute when clicked
        file_menu.add_command(label="Quit", command=self.quit_app)

        # Add the pull down menu to the menu bar
        the_menu.add_cascade(label="File", menu=file_menu)

        # Display the menu bar
        root.config(menu=the_menu)


root = Tk()

text_editor = TextEditor(root)

root.mainloop()