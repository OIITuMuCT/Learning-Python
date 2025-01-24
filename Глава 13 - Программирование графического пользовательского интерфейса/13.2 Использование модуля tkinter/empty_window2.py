# Эта программа показывает пустое окно.

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
    
    tkinter.mainloop()

if __name__ == "__main__":
    my_guy = MyGUI()