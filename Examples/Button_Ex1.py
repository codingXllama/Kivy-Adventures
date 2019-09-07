# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
 
Label:
#Creating 
    Button:
        text:'btn1'
        font_size:32
        color:0.8,0.9,0,1
        pos:50,100
        size:100,200
        
    Button:
        text:'btn2'
        font_size:40
        color:0.1,0.9,0.5,1
        size:200,100
        pos:200,100
                                
                                
                                
                                
"""))
