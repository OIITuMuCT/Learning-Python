# Эта программа соединяет несколько точек отрезками прямой.
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создать виджет Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Нарисовать две прямые.
        self.canvas.create_rectangle(20, 20, 180, 180)
        self.canvas.pack()
        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
