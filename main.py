from tkinter import *
from tkinter.ttk import *
import matplotlib as mpl

#function to center the window on program startup
def center_window(window):
    window.update_idletasks()
    width =window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x=(screen_width-width)//2
    y=(screen_height-height)//2
    window.geometry(f"{width}x{height}+{x}+{y}")




master = Tk()
master.geometry("800x600")
center_window(master)
class Income:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Income({self.value})"
    
class Expense:
    
    def __init__(self, value):
        self.value = value    
    def __repr__(self):
        return f"Expense({self.value})"
    
    
class Budget:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Budget({self.value})"

master.mainloop()