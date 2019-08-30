from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
FloatLayout:
    orientation:'Horizontal'
    Button:
        text:"Nuca"
        size_hint: 0.2, 0.4
        pos_hint: {'y':.4}
        
                                """))
