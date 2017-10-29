from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import FocusBehavior
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
         print(self.street.text)
         print(self.buildingNumber.text)

         self.zButaWjezdzam()


    def zButaWjezdzam(self):
        print("Wjeżdżajcie")
        print(self.selected)


    def __init__(self, dupa, **kwargs):
        super(ChooseColumns, self).__init__(**kwargs)
        self.hhh = {}
        self.selected = []
        self.check_ref = {}
        self.street = None
        self.buildingNumber = None

        def get_r():
            return self.selected, 4, None

        content = GridLayout()
        self.popup = popup = Popup(title="Choose header rows", content=content, size_hint = (None,None), size=(700,500))

        heders = csv_loadHeader(dupa[0])
        print(heders)
        self.hhh = heders

        content.cols = 6
        for i in enumerate(heders):
            # print(i)
            cbx = CheckBox()
            self.check_ref["cb" + str(i[1])] = cbx
            content.add_widget(cbx)
            content.add_widget(Label(text=str(i[0])+ " " + i[1]))
        btn1 = Button(text="Analysis")

        # txtField = TextInput(hint_text="ulica", input_filter=int)
        txtField = TextInput(input_filter = 'int', hint_text = 'Ulica: ')

        # txtField = TextInput(hint_text="ulica")
        txtField2 = TextInput(input_filter='int', hint_text='Nr Domu: ')

        content.add_widget(btn1)
        content.add_widget(Label(text="Wybor ulicy:"))
        content.add_widget(txtField)
        content.add_widget(Label(text="Wybor budynku, jesli osobny naglowek"))
        content.add_widget(txtField2)
        self.street = txtField
        self.buildingNumber = txtField2
        btn1.bind(on_press=self.getcheckboxes_active)
        popup.open()





