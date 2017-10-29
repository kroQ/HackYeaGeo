import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from ui.choose_columns import ChooseColumns
import win32api


class FilePopup(Popup):
    def __init__(self, **kwargs):
        super(FilePopup, self).__init__(**kwargs)
        self.title = "Choose file"

        # create popup layout containing a boxLayout
        content = BoxLayout(orientation='vertical', spacing=5)
        self.popup = popup = Popup(title=self.title,
                                   content=content, size_hint=(None, None), size=(600, 400))
        self.fileChooser = fileChooser = FileChooserListView(size_hint_y=None)

        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]

        def test(drive):
            # first, create the scrollView

            fileChooser.path = drive
            fileChooser.bind(on_submit=self._validate)
            fileChooser.height = 500  # this is a bit ugly...
            scrollView.add_widget(fileChooser)

            # construct the content, widget are used as a spacer
            content.add_widget(Widget(size_hint_y=None, height=5))
            content.add_widget(scrollView)
            content.add_widget(Widget(size_hint_y=None, height=5))

            # 2 buttons are created for accept or cancel the current value
            btnlayout = BoxLayout(size_hint_y=None, height=50, spacing=5)
            btn = Button(text='Ok')
            btn.bind(on_release=self._validate)
            btnlayout.add_widget(btn)

            btn = Button(text='Cancel')
            btn.bind(on_release=popup.dismiss)
            btnlayout.add_widget(btn)
            content.add_widget(btnlayout)
            dropdown.clear_widgets()
            mainbutton.clear_widgets()
            mainbutton.disabled
            mainbutton.text = drive

        dropdown = DropDown()
        for index in drives:
            btn = Button(text=index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: test(btn.text))
            dropdown.add_widget(btn)

        self.scrollView = scrollView = ScrollView()

        mainbutton = Button(text='Drive', size_hint_y=None, height=44)
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        content.add_widget(mainbutton)

        # all done, open the popup !
        popup.open()

    def _validate(self, dupa):
        self.popup.dismiss()
        self.popup = None
        Window.size = (700, 500)
        # print(self.fileChooser.selection)
        ChooseColumns.readPath(self.fileChooser.selection)
