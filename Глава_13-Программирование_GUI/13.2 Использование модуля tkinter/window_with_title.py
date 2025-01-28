# Эта программа показывает пустое окно.

import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        # Показать заголовок.
        self.main_window.title('Мой первый GUI')

    tkinter.mainloop()


if __name__ == "__main__":
    my_guy = MyGUI()
