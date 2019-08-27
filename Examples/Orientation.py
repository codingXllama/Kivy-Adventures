from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_string("""

<BoxLayout>:
    orientation:'vertical'
    Button:
        text: 'B1'
        # color:'red'
    Button:
        text: 'B2'
    Button:
        text: 'B3'
    
    

""")
class myList(BoxLayout):
    pass

# To display the class
if __name__ =="__main__":
    runTouchApp(myList())
