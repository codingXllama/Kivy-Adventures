# Example of using Relative Layout


from kivy.lang import Builder
from kivy.base import runTouchApp


runTouchApp(Builder.load_string("""
                                
RelativeLayout:

    Button:
        text:'Hello'
        size_hint: 0.3, 0.3
        pos: 50, 100
        
    
    Button:
        text: 'Bye'
        size_hint: 0.5, 0.2
        pos_hint: {'x':0.3, 'y':0.75}
                                
                                
                                
                                """))
