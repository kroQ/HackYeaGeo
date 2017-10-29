from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from data import csv_loadHeader
from kivy.uix.popup import Popup
import csv


class ChooseColumns(GridLayout):
    #
    # def readPath(dupa):
    #     heders = csv_loadHeader(dupa[0])
    #     print(heders)
    #     ChooseColumns()

    def zButaWjezdzam(self):
        return None

    def __init__(self, dupa, **kwargs):
        super(ChooseColumns, self).__init__(**kwargs)
        content = GridLayout()
        self.popup = popup = Popup(title="Choose header rows", content=content, size_hint = (None,None), size=(700,500))


        heders = csv_loadHeader(dupa[0])
        print(heders)

        content.cols = 6
        for i in heders:
            content.add_widget(CheckBox())
            content.add_widget(Label(text=i))
        popup.open()

        # super(ChooseFile, self).__init__(**kwargs)
        # self.cols = 1
        # self.add_widget(Label(text='Choose the file.'))
        # btn = Button(text="Choose")
        # self.add_widget(btn)
        # btn.bind(on_press=callback)





