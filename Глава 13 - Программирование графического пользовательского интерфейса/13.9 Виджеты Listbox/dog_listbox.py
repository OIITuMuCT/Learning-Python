# Эта программа получает выбранный пользователем вариант из виджета Listbox.
import tkinter
import tkinter.messagebox

class ListBoxSelection:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # Создать виджет Listbox.
        self.dog_listbox = tkinter.Listbox(
            self.main_window, width=0, height=0)
        self.dog_listbox.pack(padx=10, pady=5)

        dogs = ['Лабрадор', 'Пудель', 'Дог','Терьер']

        for dog in dogs:
            self.dog_listbox.insert(tkinter.END, dog)
        
        self.get_button = tkinter.Button(
            self.main_window, text="Получить элемент",
            command=self.__retrieve_dog
        )
        self.get_button.pack(padx=10, pady=5)
        tkinter.mainloop()

    def __retrieve_dog(self):
        indexes = self.dog_listbox.curselection()

        if (len(indexes) > 0):
            tkinter.messagebox.showinfo(
            message=self.dog_listbox.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(
                message='Ни один элемент не выбран.'
        )
if __name__ == '__main__':
    listbox_selection = ListBoxSelection()