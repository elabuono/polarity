import csv
from datetime import datetime
from tkinter import *

database = '2022.csv'

class Window:
    def __init__(self, master):
        self.master = master
        self.color = StringVar(value="test")

        # Store data
        def submit():
            with open(database, 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                row = [datetime.now().strftime("%m/%d/%Y %H:%M"),
                        self.color.get(),'N','N','N','N','N','N','N','N','N','N']
                csvwriter.writerow(row)
            self.master.destroy()

        # Frames
        self.frame = Frame(self.master, width = 300, height = 300)
        self.frame.pack( padx = 10, pady = 10, side = LEFT)
        self.colorframe = Frame(self.frame, width = 250, height = 250)
        self.colorframe.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = SW)

        # Label
        self.label = Label(self.frame, text="  What color is your mood?  ", font = "Helvetica 16 italic", relief=GROOVE)
        self.label.grid(row=0, column=0,  padx = 10, pady = 10)

        # Radios/Colors
        self.radiored = Radiobutton(self.colorframe, variable = self.color, value = "red", text = "RED")
        self.radiored.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.radioorange = Radiobutton(self.colorframe, variable = self.color, value = "orange", text = "ORANGE")
        self.radioorange.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.radioyellow = Radiobutton(self.colorframe, variable = self.color, value = "yellow", text = "YELLOW")
        self.radioyellow.grid(row = 1, column = 2, padx = 5, pady = 5)
        self.radiogreen = Radiobutton(self.colorframe, variable = self.color, value = "green", text = "GREEN")
        self.radiogreen.grid(row = 1, column = 3, padx = 5, pady = 5)
        self.radioblue = Radiobutton(self.colorframe, variable = self.color, value = "blue", text = "BLUE")
        self.radioblue.grid(row = 1, column = 4, padx = 5, pady = 5)
        self.radiopurple = Radiobutton(self.colorframe, variable = self.color, value = "purple", text = "PURPLE")
        self.radiopurple.grid(row = 1, column = 5, padx = 5, pady = 5)
        self.radiopink = Radiobutton(self.colorframe, variable = self.color, value = "pink", text = "PINK")
        self.radiopink.grid(row = 1, column = 6, padx = 5, pady = 5)

        # TODO: Check boxes for mood words
        #Checkbutton(master, text="male", variable=var1).grid(row=0, sticky=W)

        # Submit
        self.Button = Button(self.frame, text = "Submit", command = submit)
        self.Button.grid(row = 2, column = 0, sticky = E,  padx = 5, pady = 5)


def main():
    root = Tk()
    root.title("Polarity")
    window = Window(root)
    root.mainloop()

main()
