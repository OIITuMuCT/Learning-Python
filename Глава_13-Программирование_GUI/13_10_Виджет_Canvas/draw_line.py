# Эта программа демонстрирует виджет Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создать виджет Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        
        # Нарисовать две прямые.
        self.canvas.create_line(0,0,199,199)
        self.canvas.create_line(199, 0, 0, 199)
        self.canvas.pack()
        tkinter.mainloop()
    
if __name__=="__main__":
    my_gui = MyGUI()