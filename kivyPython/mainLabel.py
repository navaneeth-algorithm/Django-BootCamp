from kivy.app import App
from kivy.uix.label import Label

class Application(App):
    def build(self):
        return Label(text="Hello Navaneeth")


Application().run()