# Эта программа демонстрирует простой виджет Listbox/
import tkinter


class ListboxExample:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.listbox = tkinter.Listbox(self.main_window, height=0, width=0)
        self.listbox.pack(padx=10, pady=10)

        days = ["Понедельник", "Вторник", "Среда",
                "Четверг", "Пятница", "Суббота",
                "Воскресенье"]
        for day in days:
            self.listbox.insert(tkinter.END, day)
        
        tkinter.mainloop()

if __name__ == '__main__':
    listbox_example = ListboxExample()