import tkinter


class MyGUI:
    def __init__(self):
        # создать виджет главного окна.
        self.main_window = tkinter.Tk()
        # создать два виджета Label
        self.label1 = tkinter.Label(self.main_window, text="Hello World!")
        self.label2 = tkinter.Label(
            self.main_window, text="Это моя первая программа с GUI"
        )
        # Вызвать метод pack для обоих виджетов
        self.label1.pack(side='left')
        self.label2.pack(side='left')

        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
