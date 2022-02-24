import csv
from datetime import datetime
from os.path import exists
from tkinter import *


class Window:
    def __init__(self, master, csv_file):
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
            monthRequest = dropValue.get()
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # to skip header in our file before processing data
            for row in csv_reader:
                monthNumeric = row[0]
                if monthNumeric != '':
                    month = (datetime.strptime(monthNumeric, "%m/%d/%Y %H:%M")).strftime("%B")
                    if(month == monthRequest):
                        print(row)
            csv_file.seek(0)
            
        button = Button(master, text="SUBMIT", command=submit)
        button.pack()

def main():
    # Open Data
    csv_file = open('2022.csv', 'r')
    # Open app
    root = Tk()
    root.title("Polarity View")
    window = Window(root, csv_file)
    root.mainloop()
    csv_file.close()
  
    
main()