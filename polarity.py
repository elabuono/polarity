


database = '2022.csv'
header = ['datetime','color','manic','depressive','overwhelmed','apathetic','happy','sad','irritable','calm','empty','fulfilled']

class Window:
    def __init__(self, master):
        self.master = master
        self.color = StringVar(value="BLANK")
        self.manic = BooleanVar(value="False")
        self.depressive = BooleanVar(value="False")
        self.overwhelmed = BooleanVar(value="False")
        self.apathetic = BooleanVar(value="False")
        self.happy = BooleanVar(value="False")
        self.sad = BooleanVar(value="False")
        self.irritable = BooleanVar(value="False")
        self.calm = BooleanVar(value="False")
        self.empty = BooleanVar(value="False")
        self.fulfilled = BooleanVar(value="False")

        # Store data
        def submit():
            with open(database, 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                row = [datetime.now().strftime("%m/%d/%Y %H:%M"),
                        self.color.get(), self.manic.get(),
                        self.depressive.get(), self.overwhelmed.get(),
                        self.apathetic.get(), self.happy.get(),
                        self.sad.get(), self.irritable.get(),
                        self.calm.get(), self.empty.get(),
                        self.fulfilled.get()]
                csvwriter.writerow(row)
            self.master.destroy()

        # Frames
        self.frame = Frame(self.master, width = 300, height = 300)
        self.frame.pack( padx = 10, pady = 10, side = LEFT)

        self.colorframe = Frame(self.frame, width = 200, height = 100)
        self.colorframe.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.moodframe = Frame(self.frame, width = 200, height = 200)
        self.moodframe.grid(row = 2, column = 0, padx = 10, pady = 10)


        # Label
        self.label = Label(self.frame, text="  What color is your mood?  ", font = "Helvetica 16 italic", relief=GROOVE)
        self.label.configure(bg='#808080')
        self.label.grid(row=0, column=0,  padx = 10, pady = 10)

        # Radios/Colors
        Radiobutton(self.colorframe, variable = self.color, value = "red", text = "RED").grid(row = 1, column = 0, padx = 5, pady = 5)
        Radiobutton(self.colorframe, variable = self.color, value = "orange", text = "ORANGE").grid(row = 1, column = 1, padx = 5, pady = 5)
        Radiobutton(self.colorframe, variable = self.color, value = "yellow", text = "YELLOW").grid(row = 1, column = 2, padx = 5, pady = 5)
        Radiobutton(self.colorframe, variable = self.color, value = "green", text = "GREEN").grid(row = 1, column = 3, padx = 5, pady = 5)
        Radiobutton(self.colorframe, variable = self.color, value = "blue", text = "BLUE").grid(row = 1, column = 4, padx = 5, pady = 5)
        Radiobutton(self.colorframe, variable = self.color, value = "purple", text = "PURPLE").grid(row = 1, column = 5, padx = 5, pady = 5)
        Radiobutton(self.colorframe, variable = self.color, value = "pink", text = "PINK").grid(row = 1, column = 6, padx = 5, pady = 5)

        # Check boxes for mood words
        Checkbutton(self.moodframe, text="manic", variable=self.manic).grid(row = 2, column = 1, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="depressive", variable=self.depressive).grid(row = 2, column = 2, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="overwhelmed", variable=self.overwhelmed).grid(row = 2, column = 3, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="apathetic", variable=self.apathetic).grid(row = 2, column = 4, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="happy", variable=self.happy).grid(row = 2, column = 5, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="sad", variable=self.sad).grid(row = 3, column = 1, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="irritable", variable=self.irritable).grid(row = 3, column = 2, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="calm", variable=self.calm).grid(row = 3, column = 3, padx = 5, pady = 5, ipadx = 5)
        Checkbutton(self.moodframe, text="fulfilled", variable=self.fulfilled).grid(row = 3, column = 4, padx = 5, pady = 5)
        Checkbutton(self.moodframe, text="empty", variable=self.empty).grid(row = 3, column = 5, padx = 5, pady = 5)

        # Submit
        self.Button = Button(self.frame, text = "Submit", command = submit).grid(row = 4, column = 0, sticky = E,  padx = 5, pady = 5)



def main():
    # Initialization routine if file is not found
    if not exists(database):
        new_file = open(database, 'w')
        new_database = csv.writer(new_file)
        new_database.writerow(header)
        new_file.close()
    # Open app
    root = Tk()
    root.title("Polarity")
    window = Window(root)
    root.mainloop()

main()
