from kivy.lang import Builder
from kivy.base import runTouchApp


runTouchApp(Builder.load_string("""
BoxLayout:
    Button:
        text: 'nuca'
        size_hint_x:0.5
    Button:
        text: 'foo'
        size_hint_x:1.0
    Button: 
        text: 'bar'
        size_hint_x:0.5
                                
                                """))
