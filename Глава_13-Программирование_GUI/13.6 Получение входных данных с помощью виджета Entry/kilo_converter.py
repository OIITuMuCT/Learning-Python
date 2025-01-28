# Эта программа конвертирует расстояния в километрах
# в мили. Полученный результат выводится
# в информационном диалоговом окне.

import tkinter

import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self):
        # создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки, чтобы сгруппировать виджеты.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать виджеты для верхней рамки
        self.prompt_label = tkinter.Label(
            self.top_frame, text="Введите расстояние в километрах:"
        )
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # Упаковать виджеты для верхней рамки.
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")
        
        # Создать виджеты Button для нижней рамки.
        self.calc_button = tkinter.Button(
            self.bottom_frame, text="Преобразовать", command=self.convert
        )
        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Выйти", command=self.main_window.destroy
        )
        # Упаковать кнопки.
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Упаковать рамки
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214
        tkinter.messagebox.showinfo(
            "Результаты",
            str(kilo) + "километров эквивалентно " + str(miles) + " милям.",
        )


if __name__ == "__main__":
    kilo_conv = KiloConverterGUI()
