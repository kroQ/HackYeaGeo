from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from ui.file_popup import FilePopup
from kivy.core.window import Window


class ChooseFile(GridLayout):

    def __init__(self, **kwargs):

        def callback(instance):
            Window.size = (700, 500)
            FilePopup()

        super(ChooseFile, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Choose the file.'))
        btn = Button(text="Choose")
        self.add_widget(btn)
        btn.bind(on_press=callback)





