from tkinter import *

class Character(object):
    def __init__(self, name):
        self.name = name

    def print_text(self):
        print("Hello world!")

my_object = Character('Name')

#   Main rootWindow
rootWindow = Tk()

my_label = Label(rootWindow, text=my_object.print_text())
my_label.pack()

rootWindow.mainloop()