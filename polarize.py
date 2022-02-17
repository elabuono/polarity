import numpy as np
from pandastable import Table, TableModel
from IPython.display import display
import tkinter as tk

# polarize data
# we want to open csv and generate a visual of the data collected
# https://pandas.pydata.org/
filepath = '2022.csv'

root = tk.Tk()
root.geometry('800x400')
root.title('Polarity Data')

class TestApp(tk.Frame):
    def __init__(self, parent, filepath):
        super().__init__(parent)
        self.table = Table(self, showtoolbar=True, showstatusbar=True)
        self.table.importCSV(filepath)
        self.table.show()

app = TestApp(root, filepath)
app.pack(fill=tk.BOTH, expand=1)

root.mainloop()