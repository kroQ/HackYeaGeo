from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class TheEnd(GridLayout):

    def __init__(self, **kwargs):
        super(TheEnd, self).__init__(**kwargs)

        content = GridLayout()
        self.popup = popup = Popup(title="The End", content=content, size_hint = (None,None), size=(700,500))
        content.cols = 1
        content.add_widget(Label(text='Proces analizowania danych zakończony', font_size='25sp'))
        content.add_widget(Label(text='SUKCESEM', font_size='50sp'))
        popup.open()
