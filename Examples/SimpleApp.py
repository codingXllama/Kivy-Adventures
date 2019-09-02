from kivy.app import App

# Allows us to change screen res and size, change and rotate the image size and much more
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
# allows us to work with different screen res
from kivy.uix.floatlayout import FloatLayout


class SimpleApp(App):
    def build(self):
        myFloatLayout = FloatLayout()
        myScatter = Scatter()
        myLabel = Label(text="Welcome", font_size=110)

        myFloatLayout.add_widget(myScatter)
        myScatter.add_widget(myLabel)
        return myFloatLayout

#
if __name__ == "__main__":
    SimpleApp().run()
