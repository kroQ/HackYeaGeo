import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class FilePopup(Popup):
    def __init__(self, **kwargs):
        super(FilePopup, self).__init__(**kwargs)

        # create popup layout containing a boxLayout
        content = BoxLayout(orientation='vertical', spacing=5)
        self.popup = popup = Popup(title=self.title,
                                   content=content, size_hint=(None, None), size=(600, 400))

        # first, create the scrollView
        self.scrollView = scrollView = ScrollView()

        # then, create the fileChooser and integrate it in the scrollView
        self.fileChooser = fileChooser = FileChooserListView(size_hint_y=None)
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

        # all done, open the popup !
        popup.open()

    def _validate(self, fileChooserInstance, selected, touch):
        value = selected[0]
        self.popup.dismiss()
        self.popup = None
        # if the value was empty, don't change anything.
        if value == '':
            # do what you would do if the user didn't select any file
            return

        # do what you would do if the user selected a file.
        print
        'choosen file: %s' % value
