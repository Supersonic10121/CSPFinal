import matplotlib.pyplot as plt
import numpy as np

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #define with a name of your choosing
    def placeholder(self, file):
        try:
        # save the model
        self.model.file = file
        self.model.save()
        # show a success message
        self.view.show_success(f'The email {file} saved!')
