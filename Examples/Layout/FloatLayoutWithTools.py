from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
FloatLayout:
    orientation:'horizontal'
    padding: 100
    space: 10
    Button:
        text: 'Hello'
    Button:
        text: 'Goodbye'                               
                                """))


class myApp(FloatLayout):
    pass


if __name__ == "__main__":
    runTouchApp(myApp())
