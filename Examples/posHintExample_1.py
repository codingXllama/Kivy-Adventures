from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string(
    """
FloatLayout:
    Button:
        text: 'Hello'
        size_hint: 0.2, 0.4
        pos_hint:{'down': 1, 'lift': 1}
    
        
    
    """
))
