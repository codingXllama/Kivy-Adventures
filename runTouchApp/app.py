from kivy.base import runTouchApp
from kivy.lang import Builder

# Creating a runTouchApp with a builder to allow us to add string
runTouchApp(Builder.load_string("""


StackLayout:
    # this is a button that allows us to add touch ability of our code
    Button:
        text:'S1'



"""))