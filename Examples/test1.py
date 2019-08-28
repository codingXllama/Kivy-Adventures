from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout


Builder.load_string("""
                    
<BoxLayout>:
    orientation:'horizontal'
    
    Button:
        text: 'Hello'
        font_size: 50
        background_color: 1,2,3,0
        font_color: 11,2,0,1
        
    Button: 
        text: 'Goodbye'
        # size_hint_x: 1.0
        
     """)


class myApp(BoxLayout):
    pass


if __name__ == "__main__":
    runTouchApp(myApp())
