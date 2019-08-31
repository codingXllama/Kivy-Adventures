from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp


runTouchApp(Builder.load_string("""

BoxLayout:
    orientation: 'vertical'
    spacing: 10
    padding: 100
    Button:
        text:'Hello'
    Button:
        text: 'Goodbye'


"""))
