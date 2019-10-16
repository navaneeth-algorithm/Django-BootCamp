from kivy.app import App
from kivy.uix.button import Label


class Application(App):

    def build(self):
        return Label(text="[u][color=ff0066][b]Welcome[/b][/color][i][color=ff4455]EveryOne[/color][/i][/u]",markup=True)
    

Application().run()