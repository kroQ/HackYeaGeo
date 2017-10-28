from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class ChooseFile(GridLayout):

    def __init__(self, **kwargs):
        super(ChooseFile, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Choose the file.'))
        self.add_widget(Button(text="Choose"))

