from kivy.uix.label import Label
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
)
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (310,580)


kv = """
#:import NoTransition kivy.uix.screenmanager.NoTransition
MDFloatLayout:
    md_bg_color: 207/256,185/256,151/256,1
    
    
    ScreenManager:
        id: scr
        transition: NoTransition()
        MDScreen:
            name: "home"
            MDLabel:
                text: "Home"
                pos_hint: {"center_y": .5}
                halign: "center"
                
        MDScreen:
            name: "Calc"
            MDLabel:
                text: "Strikke omregner"
                pos_hint: {"center_x":.5, "center_y":.92}
                font_name: "Comic"
                font_size: "28sp"
                halign: "center"
            MDLabel:
                text: "Udregn hvor meget du strikker forkert med at indtaste oplysningerne nedenfor."
                pos_hint: {"center_x":.5, "center_y":.85}
                font_size: "12sp"
                font_name: "Comic"
                halign: "center"
                
                
            MDFloatLayout:
                size_hint: .9,.1
                pos_hint: {"center_x": .5, "center_y": .75}
                canvas:
                    Color: 
                        rgb: 232/256, 220/256, 202/256, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [6]
            
                TextInput:
                    id: antal_masker
                    hint_text: "Strikkeprøvens masker"
                    size_hint: .9,None
                    pos_hint: {"center_x":0.5, "center_y": .3}
                    font_name: "Comic"
                    font_size: "20sp"
                    hint_text_color: 207/256,185/256,151/256,1
                    background_color :1,1,1,0
                    padding: 18
                    cursor_color : 0,0,0,1
                    multiline: False
                    
                    
            
                        
            MDFloatLayout:
                size_hint: .9,.1
                pos_hint: {"center_x": .5, "center_y": .64}
                canvas:
                    Color: 
                        rgb: 232/256, 220/256, 202/256, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [6]

                TextInput:
                    id: opskrift_masker
                    hint_text: "Opskriftens masker"
                    size_hint: .9,None
                    pos_hint: {"center_x":0.5, "center_y": .3}
                    font_name: "Comic"
                    font_size: "20sp"
                    hint_text_color: 207/256,185/256,151/256,1
                    background_color :1,1,1,0
                    padding: 18
                    cursor_color : 0,0,0,1
                    multiline: False
                    
                    
            
            MDFloatLayout:
                size_hint: .9,.1
                pos_hint: {"center_x": .5, "center_y": .45}
                canvas:
                    Color: 
                        rgb: 232/256, 220/256, 202/256, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [6]

                TextInput:
                    id: hvad_sagde_opskriften
                    hint_text: "Opskriftens masker"
                    size_hint: .9,None
                    pos_hint: {"center_x":0.5, "center_y": .3}
                    font_name: "Comic"
                    font_size: "20sp"
                    hint_text_color: 207/256,185/256,151/256,1
                    background_color :1,1,1,0
                    padding: 18
                    cursor_color : 0,0,0,1
                    multiline: False
                    
                    
                
                
        MDScreen:
            name: "search"
            MDLabel:
                text: "search"
                pos_hint: {"center_y": .5}
                halign: "center"
                
        MDScreen:
            name: "last"
            MDLabel:
                text: "last"
                pos_hint: {"center_y": .5}
                halign: "center"
    NavBar:
        size_hint: 0.85 , .1
        pos_hint : {"center_x":0.5, "center_y":.1}
        elevation: 10
        md_bg_color: 207/256,185/256,151/256,1
        radius:  [16]
        MDGridLayout:
            cols:4
            size_hint_x: .9
            spacing : 8
            pos_hint: {"center_x":.5 , "center_y":.5}
            MDIconButton:
                id: nav_icon1
                icon: "home"
                ripple_scale : 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 1,0,0,1
                on_release:
                    scr.current="home"
                    app.change_color(self)
                    
            MDIconButton:
                id: nav_icon2
                icon: "calculator"
                ripple_scale : 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                on_release:
                    scr.current="Calc"
                    app.change_color(self)
                
            MDIconButton:
                id: nav_icon3
                icon: "creation"
                ripple_scale : 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                on_release:
                    scr.current="search"
                    app.change_color(self)
                
            MDIconButton:
                id: nav_icon4
                icon: "folder"
                ripple_scale : 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                on_release:
                    scr.current="last"
                    app.change_color(self)
"""

class NavBar(CommonElevationBehavior,MDFloatLayout):
    pass


class SimpleKivyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
    def change_color(self,instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(4):
                if f"nav_icon{i+1}" == current_id:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 1,0,0,1
                else:
                    
                    self.root.ids[f"nav_icon{i+1}"].text_color = 0,0,0,1

SimpleKivyApp().run()
