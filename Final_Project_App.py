from model import File
from view import View
from controller import Controller
import tkinter as tk


class APP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CS Problem Solving Final Project")
        userFile = File('sample_file.wav')
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = Controller(userFile, view)
        view.set_controller(controller)

        if __name__ == '__main__':
            app = App()
            app.mainloop()
