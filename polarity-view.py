import csv
from datetime import datetime
from os.path import exists
from tkinter import *


class Window:
    def __init__(self, master, csv_reader):
        self.master = master
        
        dropValue = StringVar(master)
        dropValue.set("MONTH") # default value

        monthDropDown = OptionMenu(master, dropValue, 
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
        )
        monthDropDown.pack()
        
        
        def submit():
            print ("value is: " + dropValue.get())
            for row in csv_reader:
                monthNumeric = row[0:1]
                if monthNumeric != '':
                    print(monthNumeric)
            
        button = Button(master, text="SUBMIT", command=submit)
        button.pack()

def main():
    # Open Data
    csv_reader = csv.reader(open('2022.csv', 'r'))
    # Open app
    root = Tk()
    root.title("Polarity View")
    window = Window(root, csv_reader)
    root.mainloop()
  
    
main()