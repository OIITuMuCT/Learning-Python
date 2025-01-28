# Эта программа демонстрирует виджет Button
# Когда пользователь нажимает на кнопку Button,
# на экран выводится информационное диалоговое окно
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создать виджет Button
        # На кнопке должен появиться текст "Нажми меня!".
        # должен быть исполнен метод do_something.1
        self.my_button = tkinter.Button(self.main_window, 
                                        text='Нажми меня!',
                                        command=self.do_something)

        self.my_button.pack()

        tkinter.mainloop()
        # Метод so_something является функцией обратного
        # вызова для виджета Button.
    def do_something(self):
        # Показать информационной диалоговое окно.
        tkinter.messagebox.showinfo('Реакция', 'Благодарю, что нажали кнопку.')

if __name__ == "__main__":
    my_gui = MyGUI()
