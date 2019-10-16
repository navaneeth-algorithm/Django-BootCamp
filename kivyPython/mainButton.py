from kivy.app import App
from kivy.uix.button import Button
from functools import partial

class Application(App):
    def disableButton(self,instance,*args):
        instance.disable = True
    
    def update(self,instance,*args):
        instance.text = "Hey i am disabled"
        
    def build(self):
        mybtn = Button(text="Press me",pos=(300,350),size_hint=(.25,.18))
        mybtn.bind(on_press=partial(self.disableButton,mybtn))
        mybtn.bind(on_press=partial(self.update,mybtn))
        return mybtn
    
Application().run()