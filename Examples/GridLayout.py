from kivy.lang import Builder
from kivy.base import runTouchApp


runTouchApp(Builder.load_string("""
    
GridLayout:
    rows:2
    size_hint_x:None
    spacing:10
    padding:5
    
    
    Button:
        text:'hi'
        size_hint_x:None
        width:200
    Button:
        text: 'bye'
        size_hint_x:None
        width: 100
    
    Button:
        text: 'Hello'
        width: 100
    # Button: 
    #     text: 'cya'   
    #     # width: 100
    
    # Button: 
    #     text: 'idk'  
    #     # width: 100                       
                                
                                
                                """))
