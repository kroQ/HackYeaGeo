from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainFrame(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MainFrame().run()
    