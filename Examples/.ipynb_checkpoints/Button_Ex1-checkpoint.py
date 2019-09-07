# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
 
Label:
    Button:
        text: 'Btn1'
        font_size:20
        color: 0.8,0.9,0,1
        pos: 50,300                               
                                
                                
                                
                                
                                """))
