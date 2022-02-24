import csv
from datetime import datetime
from os.path import exists
from tkinter import *


class Window:
    def __init__(self, master):
        self.master = master
        
        defaultvalue = StringVar(master)
        defaultvalue.set("Month...") # default value

        monthDropDown = OptionMenu(master, defaultvalue, 
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
        )
        monthDropDown.pack()

def main():
    # Open app
    root = Tk()
    root.title("Polarity View")
    window = Window(root)
    root.mainloop()
    
main()