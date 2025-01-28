# Эта программа демонстрирует виджет Listbox с горизонтальной прокруткой. 
import tkinter

class HorizontalScrollbarExample:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        self.listbox = tkinter.Listbox(
            self.listbox_frame, height=0, width=30)
        self.listbox.pack(side='top')

        self.scrollbar = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.HORIZONTAL)
        self.scrollbar.pack(side='bottom', fill=tkinter.X)
        
        self.scrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar.set)
        
        # Create list
        data = [
            'Небоскреб Бурджа-Халифа имеет высоту 2717 футов.',
            'Шанхайская башня имеет высоту 2073 фута.',
            'Часовая башня Абрадж аль-Бейт имеет высоту 1971 фут.',
            'Финансовый центр Пинань имеет высоту 1965 футов.']
        # заполнить виджет Listbox данными
        for element in data:
            self.listbox.insert(tkinter.END, element)
        
        tkinter.mainloop()

if __name__ == "__main__":
    scrollbar_example = HorizontalScrollbarExample()