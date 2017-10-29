from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from data import csv_loadHeader
import csv


class ChooseColumns(GridLayout):

    def readPath(dupa):
        heders = csv_loadHeader(dupa[0])
        print(heders)

    def zButaWjezdzam(self):
        return None

    def __init__(self, **kwargs):

        super(ChooseFile, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Choose the file.'))
        btn = Button(text="Choose")
        self.add_widget(btn)
        btn.bind(on_press=callback)





