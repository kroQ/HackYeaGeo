from kivy.app import App
from ui.choose_file import ChooseFile
from kivy.core.window import Window


class Main(App):

    def build(self):
        Window.size = (300, 150)
        return ChooseFile()


if __name__ == '__main__':
    Main().run()
