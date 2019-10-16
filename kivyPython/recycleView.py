from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder

Builder.load_string('''
 
<viewRecycle>:
 
    viewclass: 'Button'
    
    RecycleBoxLayout:
    
        size_hint_y: None
        
        height: self.minimum_height
        
        orientation: 'vertical'
        
''')

class viewRecycle(RecycleView):
    def __init__(self,**kwargs):
        super(viewRecycle,self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]

class RecycleApp(App):
    def build(self):
        return viewRecycle()
RecycleApp().run()