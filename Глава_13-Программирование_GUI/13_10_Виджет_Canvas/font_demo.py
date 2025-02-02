# Эта программа наносит текст на виджет Canvas.
import tkinter
import tkinter.font


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создать виджет Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        
        # Создать объект Font
        myfont = tkinter.font.Font(family='Helvetica', size=18, weight='bold')
        
        # Показать немного текста.
        self.canvas.create_text(100, 100, text="Hello World!", font=myfont)
        
        # Упаковать холст.
        self.canvas.pack()
        # Запустить главный цикл.
        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
