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

    def getcheckboxes_active(self, *arg):
         for idx, wgt in enumerate(self.check_ref.items()):
            if wgt[1].active:
                self.selected.append(idx)

         self.zButaWjezdzam()


    def zButaWjezdzam(self):
        print("Wjeżdżajcie")
        print(self.selected)


    def __init__(self, dupa, **kwargs):
        super(ChooseColumns, self).__init__(**kwargs)
        self.hhh = {}
        self.selected = []
        self.check_ref = {}

        def get_r():
            return self.selected, 4, None

        content = GridLayout()
        self.popup = popup = Popup(title="Choose header rows", content=content, size_hint = (None,None), size=(700,500))

        heders = csv_loadHeader(dupa[0])
        print(heders)
        self.hhh = heders

        content.cols = 6
        for i in heders:
            cbx = CheckBox()
            self.check_ref["cb" + str(i)] = cbx
            content.add_widget(cbx)
            content.add_widget(Label(text=i))
        btn1 = Button(text="Analysis")
        content.add_widget(btn1)
        btn1.bind(on_press=self.getcheckboxes_active)
        popup.open()





