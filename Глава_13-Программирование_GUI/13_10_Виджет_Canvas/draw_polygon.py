# Эта программа рисует два овала на виджете Canvas.
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создать виджет Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Нарисовать две прямые.
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100,
                                   100, 140, 60, 140, 20, 100, 20, 60)

        self.canvas.pack()
        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
