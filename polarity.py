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

        # Frame
        self.frame = Frame(self.master, width = 400, height = 400)
        self.frame.pack()

        # Radiobutton

        self.radiored = Radiobutton(self.frame, variable = self.color, value = "red", text = "RED")
        self.radiored.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 20)

        self.radioblue = Radiobutton(self.frame, variable = self.color, value = "blue", text = "BLUE")
        self.radioblue.grid(row = 0, column = 1, sticky = W, pady = 20)

        self.radiogreen = Radiobutton(self.frame, variable = self.color, value = "green", text = "GREEN")
        self.radiogreen.grid(row = 0, column = 1, sticky = W, pady = 20)

        self.Button = Button(self.frame, text = "Submit", command = submit)
        self.Button.grid(row = 1, column = 1, sticky = E, padx = 20, pady = 20)


def main():
    root = Tk()
    root.title("Polarity")
    window = Window(root)
    root.mainloop()

main()
