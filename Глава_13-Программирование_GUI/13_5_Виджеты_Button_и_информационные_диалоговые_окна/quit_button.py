import tkinter

import tkinter.messagebox

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window,
                                        text='Нажми меня!!!',
                                        command=self.do_something)
        # Создать кнопку "Выйти". при нажатии на которую вызывается 
        # метод destroy корневого виджета (переменная 
        # main_window ссылается на корневой виджет, поэтому функцией 
        # обратного вызова является self.main_window.destroy.)
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Выйти',
                                          command=self.main_window.destroy)
        
        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Реакция',
                                    'Благодарю что нажали кнопку.')

if __name__ == '__main__':
    my_gui = My_GUI()