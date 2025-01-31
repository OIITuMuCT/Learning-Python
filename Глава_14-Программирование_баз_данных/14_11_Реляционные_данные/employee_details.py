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

    # Создать надпись с подсказкой для пользователя
    def __create_prompt_label(self):
        self.employee_prompt_label = tkinter.Label(
            self.main_window, text= 'Выберите сотрудника'
        )
        self.employee_prompt_label.pack(side='top', padx=5, pady=5)
    # Скомпоновать рамку, содержащую виджеты Listbox и Scrollbar.
    def __build_listbox_frame(self):
        # создать рамку для виджетов Listbox Scrollbar.
        self.listbox_frame = tkinter.Frame(self.main_window)
        
        # Настроить виджет Listbox.
        self.__setup_listbox()
        
        # Создать полосу прокрутки для просмотра элементов в виджете Listbox
        self.__create_scrollBar()
        
        # Заполнить виджет Listbox именами сотрудников. 
        self.__populate_listbox()

        # Упаковать рамку виджета Listbox
        self.listbox_frame.pack()

    # Создать виджет Listbox для вывода имен сотрудников на экран
    def __setup_listbox(self):
        