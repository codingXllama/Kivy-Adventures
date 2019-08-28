from kivy.lang import Builder
from kivy.base import runTouchApp


runTouchApp(Builder.load_string("""

FloatLayout:
    Button:
        text:'Float'
        # Using size_hint, and size_hint_y
        
        # size_hint:1.0 ,0.1
        # size_hint_y:0.2
        
        #using size_hint_max_x  , note you must include the 'None' key word with no ''
        size_hint_max_x:None
        size_hint_y:0.3
                                
                                
                                
   """))
