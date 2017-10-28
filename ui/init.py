from kivy.app import App
from ui.choose_file import ChooseFile


class Init(App):

    def build(self):
        return ChooseFile()


if __name__ == '__main__':
    Init().run()
