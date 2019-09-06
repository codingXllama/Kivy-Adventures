# Purpose: To display how the StackLayout works

from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
   
   
StackLayout:
    orientation: 'rl-bt'
    spacing:10
    padding:20
    Button:
        text:'Hi'
        size_hint: .2,.3
    Button:
        text:'Bye'   
        size_hint: .2,.3                          
                                
                                
                                """))
