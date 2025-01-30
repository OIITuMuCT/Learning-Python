import tkinter
import tkinter.messagebox
import sqlite3

class EmployeeDetails:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Скомпоновать содержимое главного окна.
        self.__build_main_window()
        
        # Запустить главный цикл.
        tkinter.mainloop()

    # Скомпоновать главное окно
    def __build_main_window(self):
        # создать надпись с подсказкой для пользователя.
        self.__create_prompt_label()
        
        # Скомпоновать рамку виджета Listbox/
        self.__build_listbox_frame()
        
        # Создать кнопку выйти.
        self.__create_quit_button()
