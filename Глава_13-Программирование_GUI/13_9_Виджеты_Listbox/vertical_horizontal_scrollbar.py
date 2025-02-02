# Эта программа демонстрирует виджет Listbox с горизонтальной прокруткой.
import tkinter


class ScrollbarExample:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # Создать внутреннюю рамку, которая будет содержать
        # внутреннюю рамку и горизонтальную полосу прокрутки.
        self.outer_frame = tkinter.Frame(self.main_window)
        self.outer_frame.pack(padx=20, pady=20)

        # Создать внутреннюю рамку для Listbox и вертикальную полосу прокрутки.
        self.inner_frame = tkinter.Frame(self.outer_frame)
        self.inner_frame.pack()

        # Создать виджет Listbox в рамке inner_frame
        self.listbox = tkinter.Listbox(
            self.inner_frame, height=5, width=30)
        self.listbox.pack(side="left")

        # Создать вертикальный виджет Scrollbar в рамке inner_frame.
        self.v_scrollbar = tkinter.Scrollbar(
            self.inner_frame, orient=tkinter.VERTICAL)
        self.v_scrollbar.pack(side="right", fill=tkinter.Y)

        # Создать горизонтальный виджет Scrollbar в рамке outer_frame.
        self.h_scrollbar = tkinter.Scrollbar(
            self.outer_frame, orient=tkinter.HORIZONTAL)
        self.h_scrollbar.pack(side="bottom", fill=tkinter.X)

        # Сконфигурировать виджеты Scrollbar и Listbox для совместной работы.
        self.v_scrollbar.config(command=self.listbox.yview)
        self.h_scrollbar.config(command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.v_scrollbar.set,
                            xscrollcommand=self.h_scrollbar.set)

        # Create list
        data = [
            "Небоскреб Бурджа-Халифа имеет высоту 2717 футов.",
            "Шанхайская башня имеет высоту 2073 фута.",
            "Часовая башня Абрадж аль-Бейт имеет высоту 1971 фут.",
            "Финансовый центр Пинань имеет высоту 1965 футов.",
            "Здание Goldin Finance имеет высоту 1957 футов.",
            "Башня Lotte World имеет высоту 1819 футов.",
            "Всемирный торговый центр имеет высоту 1776 футов.",
        ]
        # заполнить виджет Listbox данными
        for element in data:
            self.listbox.insert(tkinter.END, element)

        tkinter.mainloop()


if __name__ == "__main__":
    scrollbar_example = ScrollbarExample()
