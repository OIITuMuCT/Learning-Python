# Эта программа рисует два овала на виджете Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создать виджет Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Нарисовать две прямые.
        self.canvas.create_oval(20,20, 70, 70)
        self.canvas.create_oval(100, 100, 180, 130)

        self.canvas.pack()
        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
