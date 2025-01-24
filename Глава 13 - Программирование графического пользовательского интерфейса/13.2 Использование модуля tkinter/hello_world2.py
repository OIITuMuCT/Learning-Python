import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        self.label2 = tkinter.Label(self.main_window, 
                                    text='Это моя первая программа с GUI')
        self.label1.pack()
        self.label2.pack()
        
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()