# Эта программа показывает надпись с текстом.

import tkinter

class MyCUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # Создать виджет Label, содержащий надпись "Привет, мир!"
        self.label = tkinter.Label(self.main_window, text='Привет мир!')
        # вызвать метод pack() виджета Label.
        self.label.pack()
        
        tkinter.mainloop()

if __name__ =='__main__':
    my_gui = MyCUI()