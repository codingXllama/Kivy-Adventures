# AnchorLayout example

from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""

#Building the AnchorLayout

AnchorLayout:

# Adding the x and y anchor properties

    anchor_x:'left'
    anchor_y:'bottom'
    
    Button:
        text:'hi'
        size_hint: 0.5,0.5
    
    Button: 
        text: 'bye'
        size_hint: 0.3,0.1
                              
    """))
