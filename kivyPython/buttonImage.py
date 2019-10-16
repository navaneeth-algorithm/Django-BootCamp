from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
'''Builder.load_string("""
<Application>:
    Button:
        text:""
        size_hint:.12,.12
        Image:
            source:'trial.png'
            center_x:self.parent.center_x
            center_y:self.parent.center_y




""")'''
Builder.load_file('kivyEx.kv')
class Application(App,BoxLayout):

    def build(self):
        return self
    
Application().run()
