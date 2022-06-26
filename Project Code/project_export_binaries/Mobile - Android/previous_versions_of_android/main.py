import sqlite3 as sq3
import webbrowser as web
from random import randint as ran
from datetime import datetime as data

from kivy.properties import StringProperty 
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen # tela
from kivy.lang import Builder as bd # cria o metódo construir 
#from kivy.core.window import Window as tamaño_pantalla # regula o tamanho da janela
from kivy.uix.screenmanager import ScreenManager as screenManager

from kivymd.uix.dialog import *
from kivymd.uix.label import Label
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.toolbar import MDToolbar as Bar
from kivymd.uix.boxlayout import MDBoxLayout as Box
from kivymd.app import MDApp as md_application # cria a janela
from kivymd.uix.list import ThreeLineAvatarIconListItem as three_Line_List
from kivymd.uix.list import ThreeLineListItem as three_Line_List2

"""Tamaño_patalla = (400,600)
tamaño_pantalla.size = Tamaño_patalla
tamaño_pantalla.minimum_width = 400
tamaño_pantalla.minimum_height = 400"""

box = '''

<Tela1>: 
    name: 'tela1'
    
    ScrollView:

        do_scroll_x: False
        do_scroll_y: True
        
        MDGridLayout:

            rows: 2
            cols:1
            padding: 40, 40
            spacing: 90, 90
            size_hint_y: None
            height: self.minimum_height
            row_default_height: 700
            adaptive_height: True

            BoxLayout:
                orientation: 'vertical'
        
                FloatLayout:

                    MDLabel:
                        id: text_1
                        text: "1st step:".title()
                        font_style: 'H6'
                        size_hint_x: 0.9
                        pos_hint: {'center_x':0.46, 'center_y':0.88}
                        width:200
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                    MDTextField:
                        id: user
                        size_hint_x: 0.9
                        hint_text: str('User:')
                        pos_hint: {'center_x':0.5, 'center_y':0.72}
                        icon_right: 'account-edit-outline'
                        icon_right_color: app.theme_cls.primary_color
                        width:200
                        helper_text: str('Register a User').center(5)
                        helper_text_mode: "on_focus"
                        required: False

                    MDTextField:
                        id: word
                        size_hint_x: 0.9
                        hint_text: str('Choose a Word:')
                        pos_hint: {'center_x':0.5, 'center_y':0.56}
                        icon_right: 'lock-plus-outline'
                        icon_right_color: app.theme_cls.primary_color
                        width:200
                        helper_text: str('Choose a word to be part of the password').center(5)
                        helper_text_mode: "on_focus"
                        required: False

                    MDTextField:
                        id: site
                        size_hint_x: 0.9
                        hint_text: str('Website:')
                        pos_hint: {'center_x':0.5, 'center_y':0.38}
                        icon_right: 'web'
                        icon_right_color: app.theme_cls.primary_color
                        width:200
                        helper_text: str('Site or Web Platform').center(5)
                        helper_text_mode: "on_focus"
                        required: False

                    MDRectangleFlatIconButton:
                        id: button1
                        icon: "numeric-6-box"
                        size_hint_x: 0.4
                        pos_hint: {'center_x':0.25, 'center_y':0.15}
                        text: "character".upper().center(5)
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        line_color: app.theme_cls.primary_color
                        theme_icon_color: "Custom"
                        icon_color: app.theme_cls.primary_color
                        on_release:
                            root.button6(user.text, word.text, site.text)
                        
                        ripple_rad_default: 200
                        ripple_scale: .3
                        ripple_duration_in_fast: .1
                        ripple_duration_out: .0
                        ripple_duration_in_slow: 2

                    MDLabel:
                        id: label
                        text: "-or-".upper()
                        halign: "center"
                        size_hint_x: 0.9
                        font_size: 30
                        pos_hint: {'center_x':0.5, 'center_y':0.15}
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color

                    MDRectangleFlatIconButton:
                        id: button2
                        icon: "numeric-9-box"
                        size_hint_x: 0.4
                        pos_hint: {'center_x':0.75, 'center_y':0.15}
                        text: "character".upper().center(5)
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        line_color: app.theme_cls.primary_color
                        theme_icon_color: "Custom"
                        icon_color: app.theme_cls.primary_color
                        on_release:
                            root.button9(user.text, word.text, site.text)

                        ripple_rad_default: 200
                        ripple_scale: .3
                        ripple_duration_in_fast: .1
                        ripple_duration_out: .0
                        ripple_duration_in_slow: 2
                    
                    MDLabel:
                        id: text_2
                        text: "2st step:".title()
                        font_style: 'H6'
                        size_hint_x: 0.9
                        pos_hint: {'center_x':0.46, 'center_y':0.0045}
                        width:200
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                    MDCard:

                        id: card1
                        size_hint_y: None
                        height: "300dp"
                        padding: "3dp"
                        radius: 6
                        elevation: 7
                        pos_hint: {'center_x':0.5, 'center_y':-0.49}
                        md_bg_color: 0.35, 0.55, 0.65, 1

                        ScrollView:

                            do_scroll_x: False
                            do_scroll_y: True

                            MDList:
                                id: container

<Tela2>: 
    name: 'tela2'

    ScrollView:

        do_scroll_x: False
        do_scroll_y: True
        
        MDGridLayout:

            rows: 2
            cols:1
            padding: 40, 40
            spacing: 90, 90
            size_hint_y: None
            height: self.minimum_height
            row_default_height: 700
            adaptive_height: True

            BoxLayout:
                orientation: 'vertical'

                FloatLayout:

                    MDLabel:
                        id: title
                        text: "Your saved passwords:".title()
                        font_style: 'H6'
                        size_hint_x: 0.9
                        pos_hint: {'center_x':0.46, 'center_y':0.87}
                        width:200
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                    MDTextField:
                        id: search
                        size_hint_x: 0.95
                        hint_text: str('Search:')
                        pos_hint: {'center_x':0.5, 'center_y':0.673}
                        #icon_right: 'magnify'
                        #icon_right_color: app.theme_cls.primary_color
                        width:200
                        helper_text: str('find your passwords through the website or dates').center(5).title()
                        helper_text_mode: "on_focus"
                        multiline: False

                    MDRoundFlatIconButton:
                        id: button
                        icon: "magnify"
                        text: "Let's Search"
                        font_size: 30
                        pos_hint: {'center_x':0.766, 'center_y':0.523} 
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        icon_color: app.theme_cls.primary_color
                        line_color: 0, 0, 0, 0
                        on_release:
                            root.test()

                        ripple_rad_default: 0.1
                        ripple_scale: .3
                        ripple_duration_in_fast: .1
                        ripple_duration_out: .0
                        ripple_duration_in_slow: 2

                    MDCard:

                        id: card2
                        size_hint_y: None
                        height: "350dp"
                        padding: "3dp"
                        radius: 6.5
                        elevation: 7
                        pos_hint: {'center_x':0.5, 'center_y':-0.04}
                        md_bg_color: 0.35, 0.55, 0.65, 1

                        ScrollView:

                            do_scroll_x: False
                            do_scroll_y: True

                            MDList:
                                id: container2
                        

<Tela3>: 
    name: 'tela3'

    BoxLayout:
        orinetation: 'vertical'

        FloatLayout:

            MDTextButton:
                text: 'Alpha Version 0.5.0'
                pos_hint: {'center_x':0.5, 'center_y':0.065}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'tela4'
        
            Image:
                id: image
                source: 'test2.png'
                allow_stretch: True
                size_hint: .3, .3
                pos_hint: {'center_x':0.5, 'center_y':0.83}
                radius: [35, 35, 35, 35, 35]


            MDList:
                pos_hint: {'center_x':0.5, 'center_y':0.65}

               
                OneLineAvatarIconListItem:
                    pos_hint: {'center_x':0.5, 'center_y':0.99}

                    ripple_scale: .0
                    
                    MDLabel:
                        id: text_1
                        text: "Dark Mode:".title().center(20)
                        
                        size_hint_x: 0.9
                        pos_hint: {'center_x':0.65, 'center_y':0.5}
                        width:200
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color                    

                    MDSwitch:
                        pos_hint: {'center_x':0.75, 'center_y':0.5}
                        widget_style: "android"
                        width: dp(33)
                        on_active: 
                            app.check_1(*args)
                            root.manager.get_screen("tela1").check_2(*args)
                            root.manager.get_screen('tela2').check_3(*args)
                            
                        ripple_rad_default: 0.70
                        ripple_scale: .3
                        ripple_duration_in_fast: .1
                        ripple_duration_out: .0
                        ripple_duration_in_slow: 2

                OneLineAvatarIconListItem:
                    pos_hint: {'center_x':0.5, 'center_y':0.99}

                    ripple_scale: .0

                    MDLabel:
                        id: text_2
                        text: "Font size:".title().center(20)
                        
                        size_hint_x: 0.9
                        pos_hint: {'center_x':0.65, 'center_y':0.5}
                        width:200
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color

                    MDSlider:
                        id: slider
                        pos_hint: {'center_x':0.75, 'center_y':0.5}
                        size_hint: .3, .1

                        min: 20
                        max: 40
                        value: 25
                        on_active:
                            root.font_size(slider.value)
                            root.manager.get_screen('tela2').font_size(slider.value)
                            root.manager.get_screen('tela1').font_size(slider.value)

                        ripple_rad_default: 0.1
                        ripple_scale: .0
                        ripple_duration_in_fast: .1
                        ripple_duration_out: .0
                        ripple_duration_in_slow: 2


<Tela4>:
    name: 'tela4'

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:
            MDRectangleFlatIconButton:
                icon: "github"
                text: "project on github".title()
                text_color: app.theme_cls.primary_color
                line_color: 1, 1, 1, 1
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color

                pos_hint: {'center_x':0.5, 'center_y':0.23}
                ripple_rad_default: 0.70
                ripple_scale: .3
                ripple_duration_in_fast: .1
                ripple_duration_out: .01
                ripple_duration_in_slow: 2
                on_press: root.test2()

            MDRectangleFlatIconButton:
                icon: "youtube"
                text: "project on youtube".title()
                text_color: app.theme_cls.primary_color
                line_color: 1, 1, 1, 1
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color

                pos_hint: {'center_x':0.5, 'center_y':0.155}
                ripple_rad_default: 0.70
                ripple_scale: .3
                ripple_duration_in_fast: .1
                ripple_duration_out: .01
                ripple_duration_in_slow: 2
                on_press: root.test()
            
            MDRectangleFlatIconButton:
                icon: "instagram"
                text: "developer contact".title()
                text_color: app.theme_cls.primary_color
                line_color: 1, 1, 1, 1
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color

                pos_hint: {'center_x':0.5, 'center_y':0.08}
                ripple_rad_default: 0.70
                ripple_scale: .3
                ripple_duration_in_fast: .1
                ripple_duration_out: .01
                ripple_duration_in_slow: 2
                on_press: root.test3()
            
            Image:
                id: image
                source: 'test3.png'
                allow_stretch: True
                size_hint: .3, .3
                pos_hint: {'center_x':0.5, 'center_y':0.83}
                radius: [35, 35, 35, 35, 35]
            MDLabel:
                text: 'Made by:'
                pos_hint: {'center_x':0.5, 'center_y':0.73}
                halign: "center"
                font_style: 'H6'
            MDLabel:
                text: 'Saulo Ferro Maciel'
                pos_hint: {'center_x':0.5, 'center_y':0.68}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: 'Programming languages used:'.title()
                pos_hint: {'center_x':0.5, 'center_y':0.63}
                halign: "center"
                font_style: 'H6'
                
            MDLabel:
                text: '> Python <'
                pos_hint: {'center_x':0.5, 'center_y':0.57}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: '> kivylang <'
                pos_hint: {'center_x':0.5, 'center_y':0.53}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: '> SQL <'
                pos_hint: {'center_x':0.5, 'center_y':0.49}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: "Project's Goal:"
                pos_hint: {'center_x':0.5, 'center_y':0.42}
                halign: "center"
                font_style: 'H6'
                
            MDLabel:
                text: """Train Coding In Python And SQL"""
                pos_hint: {'center_x':0.5, 'center_y':0.37}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: """Explore Python Modules And Cybersecurity"""
                pos_hint: {'center_x':0.5, 'center_y':0.335}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: """Train mobile development""".title()
                pos_hint: {'center_x':0.5, 'center_y':0.3}
                halign: "center"
                font_style: 'Subtitle1'    
                
<ToolBar>:

    id:bar2
    title: "Capivara_Password"
    size_hint_y:0.058
    pos_hint: {"top": 1}
    elevation:20
    opacity: .99
    specific_text_color: [0.95,0.95,0.95, 1]
    

<CustomOneLineIconListItem>:
    IconLeftWidget:
        icon: root.icon

<MDThreeLineListItem1>:

<MDThreeLineAvatarIconListItem1>:
    IconRightWidget:
        icon: 'plus-box-multiple'
        on_press:
            root.buttonTest()

<lista_colheita_database>:

    ripple_rad_default: 0.70
    ripple_scale: .3
    ripple_duration_in_fast: .1
    ripple_duration_out: .0
    ripple_duration_in_slow: 2

    IconLeftWidget:
        icon: root.icon


<ContentNavigationDrawer>

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:

            MDTextButton:
                text: 'Alpha Version 0.5.0'
                pos_hint: {'center_x':0.5, 'center_y':0.065}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = 'tela4'

            Image:
                id: image
                source: 'test.png'
                allow_stretch: True
                size_hint: .3, .3
                pos_hint: {'center_x':0.5, 'center_y':0.85}
                radius: [36, 36, 36, 36, 36]

            MDList:
                pos_hint: {'center_x':0.5, 'center_y':0.6}

                OneLineAvatarIconListItem:
                    text: 'Generate Password'
                    
                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "tela1"
                    IconLeftWidget:
                        icon: "lock-plus"
                        on_release:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "tela1"

                OneLineAvatarIconListItem:
                    text: 'Saved Password'

                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "tela2"
                    IconLeftWidget:
                        icon: "content-save-edit"
                        on_release:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "tela2"

                OneLineAvatarIconListItem:
                    id: version
                    text: 'settings'.title()

                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "tela3"
                    IconLeftWidget:
                        icon: "cog"
                        on_release:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "tela3"
                     
<ScreenManager>:

    id: screen_manager
    Tela1:
    Tela2:
    Tela3:
    Tela4:

MDNavigationLayout:
    #x: toolbar.height 

    ScreenManager:
        id: screen_manager

    ToolBar:
        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer


             
'''

box2 = '''

<Tela1>: 
    name: 'tela1'
    
    ScrollView:

        do_scroll_x: False
        do_scroll_y: True
        
        MDGridLayout:

            rows: 2
            cols:1
            padding: 30, 30
            spacing: 40, 40
            size_hint_y: None
            height: self.minimum_height
            row_default_height: 400
            adaptive_height: True
        
            FloatLayout:

                MDLabel:
                    id: text_1
                    text: "1st step:".title()
                    font_size: 21
                    size_hint_x: 0.9
                    pos_hint: {'center_x':0.46, 'center_y':0.88}
                    width:200
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    
                MDTextField:
                    id: user
                    font_size: 18
                    size_hint_x: 0.9
                    hint_text: str('User:')
                    pos_hint: {'center_x':0.5, 'center_y':0.72}
                    icon_right: 'account-edit-outline'
                    icon_right_color: app.theme_cls.primary_color
                    width:200
                    helper_text: str('Register a User').center(5)
                    helper_text_mode: "on_focus"
                    required: False

                MDTextField:
                    id: word
                    font_size: 18
                    size_hint_x: 0.9
                    hint_text: str('Choose a Word:')
                    pos_hint: {'center_x':0.5, 'center_y':0.56}
                    icon_right: 'lock-plus-outline'
                    icon_right_color: app.theme_cls.primary_color
                    width:200
                    helper_text: str('Choose a word to be part of the password').center(5)
                    helper_text_mode: "on_focus"
                    required: False

                MDTextField:
                    id: site
                    font_size: 18
                    size_hint_x: 0.9
                    hint_text: str('Website:')
                    pos_hint: {'center_x':0.5, 'center_y':0.38}
                    icon_right: 'web'
                    icon_right_color: app.theme_cls.primary_color
                    width:200
                    helper_text: str('Site or Web Platform').center(5)
                    helper_text_mode: "on_focus"
                    required: False

                MDRectangleFlatIconButton:
                    id: button1
                    icon: "numeric-6-box"
                    size_hint_x: 0.4
                    pos_hint: {'center_x':0.25, 'center_y':0.15}
                    text: "character".upper().center(5)
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    line_color: app.theme_cls.primary_color
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        root.button6(user.text, word.text, site.text)
                    
                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                MDLabel:
                    id: label
                    text: "-or-".upper()
                    halign: "center"
                    size_hint_x: 0.9
                    font_size: 13
                    pos_hint: {'center_x':0.5, 'center_y':0.15}
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color

                MDRectangleFlatIconButton:
                    id: button2
                    icon: "numeric-9-box"
                    size_hint_x: 0.4
                    pos_hint: {'center_x':0.75, 'center_y':0.15}
                    text: "character".upper().center(5)
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    line_color: app.theme_cls.primary_color
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        root.button9(user.text, word.text, site.text)

                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2
                
                MDLabel:
                    id: text_2
                    text: "2st step:".title()
                    font_size: 21
                    size_hint_x: 0.9
                    pos_hint: {'center_x':0.46, 'center_y':0.0045}
                    width:200
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    
                MDCard:

                    id: card1
                    size_hint_y: None
                    height: "300dp"
                    padding: "3dp"
                    radius: 6
                    elevation: 7
                    pos_hint: {'center_x':0.5, 'center_y':-0.65}
                    md_bg_color: 0.35, 0.55, 0.65, 1

                    ScrollView:

                        do_scroll_x: False
                        do_scroll_y: True

                        MDList:
                            id: container

<Tela2>: 
    name: 'tela2'

    ScrollView:

        do_scroll_x: False
        do_scroll_y: True
        
        MDGridLayout:

            rows: 2
            cols:1
            padding: 30, 30
            spacing: 40, 40
            size_hint_y: None
            height: self.minimum_height
            row_default_height: 400
            adaptive_height: True
        
            FloatLayout:

                MDLabel:
                    id: title
                    text: "Your saved passwords:".title()
                    font_size: 19
                    size_hint_x: 0.9
                    pos_hint: {'center_x':0.46, 'center_y':0.87}
                    width:200
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    
                MDTextField:
                    id: search
                    size_hint_x: 0.95
                    hint_text: str('Search:')
                    pos_hint: {'center_x':0.5, 'center_y':0.673}
                    #icon_right: 'magnify'
                    #icon_right_color: app.theme_cls.primary_color
                    width:200
                    helper_text: str('find your passwords through the website or dates').center(5).title()
                    helper_text_mode: "on_focus"
                    multiline: False

                MDRoundFlatIconButton:
                    id: button
                    icon: "magnify"
                    text: "Let's Search"
                    font_size: 15.5
                    pos_hint: {'center_x':0.766, 'center_y':0.523} 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    icon_color: app.theme_cls.primary_color
                    line_color: 0, 0, 0, 0
                    on_release:
                        root.test()

                    ripple_rad_default: 0.1
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                MDCard:

                    id: card2
                    size_hint_y: None
                    height: "350dp"
                    padding: "3dp"
                    radius: 6.5
                    elevation: 7
                    pos_hint: {'center_x':0.5, 'center_y':-0.29}
                    md_bg_color: 0.35, 0.55, 0.65, 1

                    ScrollView:

                        do_scroll_x: False
                        do_scroll_y: True

                        MDList:
                            id: container2
                        

<Tela3>: 
    name: 'tela3'

    BoxLayout:
        orinetation: 'vertical'

        FloatLayout:

            MDTextButton:
                text: 'Alpha Version 0.5.0'
                pos_hint: {'center_x':0.5, 'center_y':0.065}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'tela4'
        
            Image:
                id: image
                source: 'test2.png'
                #allow_stretch: True
                size_hint: .3, .3
                pos_hint: {'center_x':0.5, 'center_y':0.83}
                radius: [35, 35, 35, 35, 35]


            MDList:
                pos_hint: {'center_x':0.5, 'center_y':0.65}

               
                OneLineAvatarIconListItem:
                    pos_hint: {'center_x':0.5, 'center_y':0.99}

                    ripple_scale: .0
                    
                    MDLabel:
                        id: text_1
                        text: "Dark Mode:".title().center(20)
                        font_size: 15
                        size_hint_x: 0.9
                        pos_hint: {'center_x':0.65, 'center_y':0.5}
                        width:200
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color                    

                    MDSwitch:
                        pos_hint: {'center_x':0.75, 'center_y':0.5}
                        widget_style: "android"
                        width: dp(33)
                        on_active: 
                            app.check_1(*args)
                            root.manager.get_screen("tela1").check_2(*args)
                            root.manager.get_screen('tela2').check_3(*args)
                            
                        ripple_rad_default: 0.70
                        ripple_scale: .3
                        ripple_duration_in_fast: .1
                        ripple_duration_out: .0
                        ripple_duration_in_slow: 2

                OneLineAvatarIconListItem:
                    pos_hint: {'center_x':0.5, 'center_y':0.99}

                    ripple_scale: .0

                    MDLabel:
                        id: text_2
                        text: "Font size:".title().center(20)
                        font_size: 15
                        size_hint_x: 0.9
                        pos_hint: {'center_x':0.65, 'center_y':0.5}
                        width:200
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color

                    MDSlider:
                        id: slider
                        pos_hint: {'center_x':0.75, 'center_y':0.5}
                        size_hint: .3, .1

                        min: 15
                        max: 22
                        value: 17
                        on_active:
                            root.font_size(slider.value)
                            root.manager.get_screen('tela2').font_size(slider.value)
                            root.manager.get_screen('tela1').font_size(slider.value)

                        ripple_rad_default: 0.1
                        ripple_scale: .0
                        ripple_duration_in_fast: .1
                        ripple_duration_out: .0
                        ripple_duration_in_slow: 2


<Tela4>:
    name: 'tela4'

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:
            MDRectangleFlatIconButton:
                icon: "github"
                text: "project on github".title()
                text_color: app.theme_cls.primary_color
                line_color: 1, 1, 1, 1
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color

                pos_hint: {'center_x':0.5, 'center_y':0.23}
                ripple_rad_default: 0.70
                ripple_scale: .3
                ripple_duration_in_fast: .1
                ripple_duration_out: .01
                ripple_duration_in_slow: 2
                on_press: root.test2()

            MDRectangleFlatIconButton:
                icon: "youtube"
                text: "project on youtube".title()
                text_color: app.theme_cls.primary_color
                line_color: 1, 1, 1, 1
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color

                pos_hint: {'center_x':0.5, 'center_y':0.155}
                ripple_rad_default: 0.70
                ripple_scale: .3
                ripple_duration_in_fast: .1
                ripple_duration_out: .01
                ripple_duration_in_slow: 2
                on_press: root.test()
            
            MDRectangleFlatIconButton:
                icon: "instagram"
                text: "developer contact".title()
                text_color: app.theme_cls.primary_color
                line_color: 1, 1, 1, 1
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color

                pos_hint: {'center_x':0.5, 'center_y':0.08}
                ripple_rad_default: 0.70
                ripple_scale: .3
                ripple_duration_in_fast: .1
                ripple_duration_out: .01
                ripple_duration_in_slow: 2
                on_press: root.test3()
            
            Image:
                id: image
                source: 'test3.png'
                #allow_stretch: True
                size_hint: .3, .3
                pos_hint: {'center_x':0.5, 'center_y':0.83}
                radius: [35, 35, 35, 35, 35]
            MDLabel:
                text: 'Made by:'
                pos_hint: {'center_x':0.5, 'center_y':0.73}
                halign: "center"
                font_style: 'H6'
            MDLabel:
                text: 'Saulo Ferro Maciel'
                pos_hint: {'center_x':0.5, 'center_y':0.68}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: 'Programming languages used:'.title()
                pos_hint: {'center_x':0.5, 'center_y':0.63}
                halign: "center"
                font_style: 'H6'
                font_size: 17
            MDLabel:
                text: '> Python <'
                pos_hint: {'center_x':0.5, 'center_y':0.57}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: '> kivylang <'
                pos_hint: {'center_x':0.5, 'center_y':0.53}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: '> SQL <'
                pos_hint: {'center_x':0.5, 'center_y':0.49}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: "Project's Goal:"
                pos_hint: {'center_x':0.5, 'center_y':0.42}
                halign: "center"
                font_style: 'H6'
                font_size: 17
            MDLabel:
                text: """Train Coding In Python And SQL"""
                pos_hint: {'center_x':0.5, 'center_y':0.37}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: """Explore Python Modules And Cybersecurity"""
                pos_hint: {'center_x':0.5, 'center_y':0.335}
                halign: "center"
                font_style: 'Subtitle1'
            MDLabel:
                text: """Train mobile development""".title()
                pos_hint: {'center_x':0.5, 'center_y':0.3}
                halign: "center"
                font_style: 'Subtitle1'    
                
<ToolBar>:

    id:bar2
    title: "Capivara_Password"
    size_hint_y:0.058
    pos_hint: {"top": 1}
    elevation:20
    opacity: .99
    specific_text_color: [0.95,0.95,0.95, 1]
    

<CustomOneLineIconListItem>:
    IconLeftWidget:
        icon: root.icon

<MDThreeLineListItem1>:

<MDThreeLineAvatarIconListItem1>:
    IconRightWidget:
        icon: 'plus-box-multiple'
        on_press:
            root.buttonTest()

<lista_colheita_database>:

    ripple_rad_default: 0.70
    ripple_scale: .3
    ripple_duration_in_fast: .1
    ripple_duration_out: .0
    ripple_duration_in_slow: 2

    IconLeftWidget:
        icon: root.icon


<ContentNavigationDrawer>

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:

            MDTextButton:
                text: 'Alpha Version 0.5.0'
                pos_hint: {'center_x':0.5, 'center_y':0.065}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = 'tela4'

            Image:
                id: image
                source: 'test.png'
                #allow_stretch: True
                size_hint: .4, .4
                pos_hint: {'center_x':0.5, 'center_y':0.85}
                radius: [36, 36, 36, 36, 36]

            MDList:
                pos_hint: {'center_x':0.5, 'center_y':0.6}

                OneLineAvatarIconListItem:
                    text: 'Generate Password'
                    
                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "tela1"
                    IconLeftWidget:
                        icon: "lock-plus"
                        on_release:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "tela1"

                OneLineAvatarIconListItem:
                    text: 'Saved Password'

                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "tela2"
                    IconLeftWidget:
                        icon: "content-save-edit"
                        on_release:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "tela2"

                OneLineAvatarIconListItem:
                    id: version
                    text: 'settings'.title()

                    ripple_rad_default: 200
                    ripple_scale: .3
                    ripple_duration_in_fast: .1
                    ripple_duration_out: .0
                    ripple_duration_in_slow: 2

                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "tela3"
                    IconLeftWidget:
                        icon: "cog"
                        on_release:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "tela3"
                     
<ScreenManager>:

    id: screen_manager
    Tela1:
    Tela2:
    Tela3:
    Tela4:

MDNavigationLayout:
    #x: toolbar.height 

    ScreenManager:
        id: screen_manager

    ToolBar:
        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer


             
'''

class dataBase():
    def conecta_banco_d_dados(self):
        self.conecta = sq3.connect('password_banco_de_Dados')
        self.cursor = self.conecta.cursor()

    def desconecta_banco_d_dados(self):
        self.conecta.close()

    def monta_banco_em_tabela(self):
        self.conecta_banco_d_dados()
        
        #Cria tabela:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS password(
                senha CHAR(40) NOT NULL,
                user CHAR(40),
                site CHAR(40),
                data CHAR(40)
                
            );
        ''')

        self.conecta.commit() 
        self.desconecta_banco_d_dados()
    
    def passwordAdd(self, value1, value2, value3, value4):
        self.conecta_banco_d_dados()

        self.cursor.execute("""INSERT INTO password (senha, user, site, data)
        VALUES (?,?,?,?)""", (value1, value2, value3, value4))
        self.conecta.commit()

        self.desconecta_banco_d_dados()

    def list_insert(self):

        lista_final = list()

        self.monta_banco_em_tabela()
        self.conecta_banco_d_dados()

        lista = self.cursor.execute(""" SELECT 
                senha,
                user,
                site,
                data
            FROM password ;""")
      
        for i in lista:
            s = ','.join(i)
            s = f'{s}'
            lista_final.append(s)

        self.desconecta_banco_d_dados()
        return lista_final

    def list_insert2(self, d):

        lista_final = list()

        self.monta_banco_em_tabela()
        self.conecta_banco_d_dados()

        lista = self.cursor.execute(""" SELECT 
                senha,
                user,
                site,
                data
            FROM password WHERE data LIKE '%s' """%d)
        
        for i in lista:
            s = ','.join(i)
            s = f'{s}'
            lista_final.append(s)

        self.desconecta_banco_d_dados()
        return lista_final
   
    def list_insert3(self, d):

        lista_final = list()

        self.monta_banco_em_tabela()
        self.conecta_banco_d_dados()

        lista = self.cursor.execute(""" SELECT 
                senha,
                user,
                site,
                data
            FROM password WHERE site LIKE '%s'; """% d)
        
        for i in lista:
            s = ','.join(i)
            s = f'{s}'
            lista_final.append(s)

        self.desconecta_banco_d_dados()
        return lista_final

    def list_insert4(self, d):

        lista_final = list()

        self.monta_banco_em_tabela()
        self.conecta_banco_d_dados()

        lista = self.cursor.execute(""" SELECT 
                senha,
                user,
                site,
                data
            FROM password WHERE user LIKE '%s'; """% d)
        
        for i in lista:
            s = ','.join(i)
            s = f'{s}'
            lista_final.append(s)

        self.desconecta_banco_d_dados()
        return lista_final

class lista_colheita_database(three_Line_List):
    text = StringProperty("")
    secondary_text = StringProperty("")
    tertiary_text = StringProperty("")
    icon = StringProperty("")

    def __int__(self):
        
        self.text
        self.secondary_text
        self.tertiary_text
        self.icon

    def data(self, text1, secondaryText, tertiaryText, label, icon1):
        self.text = text1
        self.secondary_text = secondaryText
        self.tertiary_text = tertiaryText
        self.icon = icon1

        self.add_widget(Label(text=label, font_size = 25, pos_hint= {'center_x':0.85, 'center_y':0.65}))
  
class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class MDThreeLineAvatarIconListItem1(three_Line_List, dataBase):
    text = StringProperty("")
    secondary_text = StringProperty("")
    tertiary_text = StringProperty("")
    my_dialog = None
    dictionary_Text = None

    def __int__(self):
        self.text
        self.secondary_text
        self.tertiary_text
        
    def test(self, text1, secondaryText, tertiaryText):
        self.text = text1
        self.secondary_text = secondaryText
        self.tertiary_text = tertiaryText

    def buttonTest(self):

        self.my_dialog = MDDialog(title="Save password?", size_hint = [0.6 , 0.20], pos_hint= {'center_x':0.5, 'center_y':0.66},
            auto_dismiss = False, text = f'{self.text}\n{self.secondary_text}\n{self.tertiary_text}', type="custom",
            buttons = [
                MDIconButton(
                    icon= "checkbox-multiple-marked-outline",
                    size_hint_y = 0.8,
                    size_hint_x = 0.8,
                    theme_text_color= "Custom",
                    text_color= [0, 25, 0, 1],
                    pos_hint= {'center_x':1, 'center_y':.5},
                    on_release = self.saveButton, ),
                MDIconButton(
                    icon= "close-box-multiple-outline",
                    size_hint_y = 0.8,
                    size_hint_x = 0.8,
                    theme_text_color= "Custom",
                    text_color= [25, 0, 0, 1],
                    pos_hint= {'center_x':1, 'center_y':.5},
                    on_release = self.closeButton)
            ])
        self.my_dialog.open()

    def saveButton(self, obj):
        
        data_actual = data.now()
        data_actual = data_actual.strftime("%d/%m/%Y")

        convertText = f'{self.text},{self.secondary_text},{self.tertiary_text},{data_actual}'
        convertText = convertText.split(',')

        list_key = ['text1','text2','text3','data']
        self.dictionary_Text = dict(zip(list_key,convertText))
        
        self.monta_banco_em_tabela()

        self.passwordAdd(self.dictionary_Text['text1'],self.dictionary_Text['text2'], self.dictionary_Text['text3'], self.dictionary_Text['data'] )
        self.closeButton(obj)
    
    def closeButton(self, obj):
        self.my_dialog.dismiss()

class MDThreeLineListItem1(three_Line_List2):
    text = StringProperty("")
    secondary_text = StringProperty("")
    tertiary_text = StringProperty("")

    def __int__(self):
        self.text
        self.secondary_text
        self.tertiary_text
    
    def test(self):
        self.text = "Complete the First Step:"
        self.secondary_text = "You don't need to fill in the text fields"
        self.tertiary_text = "You just need to press the button"

class ContentNavigationDrawer(Box):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    
class NavigationDrawer(Box):
    pass

class ToolBar(Bar):
    pass

class ScreenManager(screenManager):
    pass

class Tela4(Screen):
    def test(self):
        web_page = 'https://www.youtube.com/watch?v=TL6i_MWZZqY&list=PLUvyOEX2BqKdtBW_rWnEgr2eJSCkKGml4'
        web.open(web_page)

    def test2(self):
        web_page = 'https://github.com/Saulo-Ferro-Maciel/Capivara_Password'
        web.open(web_page)

    def test3(self):
        web_page = 'https://www.instagram.com/saulo_fehciel/'
        web.open(web_page)

class Tela3(Screen):

    def font_size(self, value):

        self.ids.text_1.font_size = value
        self.ids.text_2.font_size = value

class Tela2(Screen, dataBase):
   
    def test(self):
        a = None
        
        b = self.ids.container2
        b.clear_widgets()

        c = self.ids.search
        d = c.text

        a1,a2,a3,a4 = self.list_insert(),self.list_insert2(d = f'{d.rstrip("").lstrip("")}%'),self.list_insert3(d = f'{d.rstrip("").lstrip("")}%'),self.list_insert4(d = f'{d.rstrip("").lstrip("")}%')

        if d == '':
            a = a1

            for i in a:
                
                i = i.split(',')
                text1,secondaryText,tertiaryText,label,icon1 =i[0],i[1],i[2].replace('https:','').replace("/",'').rstrip('').lstrip(""),i[3],i[2].replace('www','').replace('/','').replace('.','').replace('https:','').replace("org", '').replace('br','').replace('com','').lstrip("").rstrip("")

                if icon1 in ['Site not informed','not site','site não informado','not informed','n informado','não informado']:
                    icon1 ='file-cog-outline'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['paxtuescoteiros','escout','scout','paxtu','escoteiros do brasil','escoteirosdobrasil','escoteiro','escoteiroS']:
                    icon1 ='fleur-de-lis'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['360','office 360','office','windows','microsoft','github','microsoftteams','teams','xbox']:
                    icon1 ='microsoft-windows'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['meu banco','my bank','bank','citbank','caixa','pan','inter','c6bank','nubank','will','santander','banco do brasil','itaú','itau','next','bradesco','banco']:
                    icon1 ='bank'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['escola','ifma','ceuma','ufma','.edu','edu','educação','education','educacao','uema','undb','professor','aluno','alunos','professores','usp','ufsp','ufmg','ufrj','faculdade','laboro','pitagoras']:
                    icon1 = 'school-outline'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                else:
                        teste = lista_colheita_database()
                        b.add_widget(teste)
                        teste.data(text1, secondaryText, tertiaryText, label, icon1)

            if a == []:
                icon1 ='alert-outline'
                text1 = 'Error message:'
                secondaryText ='Database not found'
                tertiaryText = 'or password not registered'
                label = 'APP message'
                teste = lista_colheita_database()
                b.add_widget(teste)
                teste.data(text1, secondaryText, tertiaryText, label, icon1)
        
        elif d.isnumeric():
            a = a2
            
            for i in a:
                
                i = i.split(',')
                text1,secondaryText,tertiaryText,label,icon1 =i[0],i[1],i[2].replace('https:','').replace("/",'').rstrip('').lstrip(""),i[3],i[2].replace('www','').replace('/','').replace('.','').replace('https:','').replace("org", '').replace('br','').replace('com','').lstrip("").rstrip("")

                if icon1 in ['Site not informed','not site','site não informado','not informed','n informado','não informado']:
                    icon1 ='file-cog-outline'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['paxtuescoteiros','escout','scout','paxtu','escoteiros do brasil','escoteirosdobrasil','escoteiro','escoteiroS']:
                    icon1 ='fleur-de-lis'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['360','office 360','office','windows','microsoft','github','microsoftteams','teams','xbox']:
                    icon1 ='microsoft-windows'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['meu banco','my bank','bank','citbank','caixa','pan','inter','c6bank','nubank','will','santander','banco do brasil','itaú','itau','next','bradesco','banco']:
                    icon1 ='bank'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['escola','ifma','ceuma','ufma','.edu','edu','educação','education','educacao','uema','undb','professor','aluno','alunos','professores','usp','ufsp','ufmg','ufrj','faculdade','laboro','pitagoras']:
                    icon1 = 'school-outline'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                else:
                        teste = lista_colheita_database()
                        b.add_widget(teste)
                        teste.data(text1, secondaryText, tertiaryText, label, icon1)

            if a == []:
                icon1 ='alert-outline'
                text1 = 'Error message:'
                secondaryText ='Database not found'
                tertiaryText = 'or password not registered'
                label = 'APP message'
                teste = lista_colheita_database()
                b.add_widget(teste)
                teste.data(text1, secondaryText, tertiaryText, label, icon1)
             
        elif d.isalnum():
            a = a3
            bb = a4
            
            for z in bb:
                a.append(z)
            
            for i in a:
                
                i = i.split(',')
                text1,secondaryText,tertiaryText,label,icon1 =i[0],i[1],i[2].replace('https:','').replace("/",'').rstrip('').lstrip(""),i[3],i[2].replace('www','').replace('/','').replace('.','').replace('https:','').replace("org", '').replace('br','').replace('com','').lstrip("").rstrip("")

                if icon1 in ['Site not informed','not site','site não informado','not informed','n informado','não informado']:
                    icon1 ='file-cog-outline'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['paxtuescoteiros','escout','scout','paxtu','escoteiros do brasil','escoteirosdobrasil','escoteiro','escoteiroS']:
                    icon1 ='fleur-de-lis'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['360','office 360','office','windows','microsoft','github','microsoftteams','teams','xbox']:
                    icon1 ='microsoft-windows'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['meu banco','my bank','bank','citbank','caixa','pan','inter','c6bank','nubank','will','santander','banco do brasil','itaú','itau','next','bradesco','banco']:
                    icon1 ='bank'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                elif icon1.lower() in ['escola','ifma','ceuma','ufma','.edu','edu','educação','education','educacao','uema','undb','professor','aluno','alunos','professores','usp','ufsp','ufmg','ufrj','faculdade','laboro','pitagoras']:
                    icon1 = 'school-outline'
                    teste = lista_colheita_database()
                    b.add_widget(teste)
                    teste.data(text1, secondaryText, tertiaryText, label, icon1)
                else:
                        teste = lista_colheita_database()
                        b.add_widget(teste)
                        teste.data(text1, secondaryText, tertiaryText, label, icon1)
            
            if a == []:
                icon1 ='alert-outline'
                text1 = 'Error message:'
                secondaryText ='Database not found'
                tertiaryText = 'or password not registered'
                label = 'APP message'
                teste = lista_colheita_database()
                b.add_widget(teste)
                teste.data(text1, secondaryText, tertiaryText, label, icon1)
          
        a1,a2,a3,a4 = None,None,None,None
        a = None

    def font_size(self, value):

        b = self.ids.title.font_size = value
        self.ids.search.font_size = value
        a = self.ids.button.font_size = value - 3

        if b <= 15:
            b = 14,3
        elif a <= 15:
            a = 14,3

    def check_3(self, checkbox, value):
        if value:
            self.ids.card2.md_bg_color = [0.169,0.169,0.169, 1]
           
        else:
           self.ids.card2.md_bg_color = [0.35, 0.55, 0.65, 1]

class Tela1(Screen):
    my_dialog = None
    t = None

    def font_size(self, value):

        b = self.ids.text_1.font_size = value
        a =self.ids.text_2.font_size = value 

        if b <= 15:
            b = 14,3
        elif a <= 15:
            a = 14,3

    def check_2(self, checkbox, value):
        if value:
            self.ids.card1.md_bg_color = [0.169,0.169,0.169, 1]
            
        else:
           self.ids.card1.md_bg_color = [0.35, 0.55, 0.65, 1]
          
    def openCard(self):

        test_Text_List_Item1 = MDThreeLineListItem1()
        self.ids.container.add_widget(test_Text_List_Item1)
        test_Text_List_Item1.test()
    
        self.ids.user.clear_widgets()
        self.ids.word.clear_widgets()
      
        self.ids.word.text = str("")
        self.ids.user.text = str('')

        self.my_dialog = MDDialog(title="Alert:", text="You cannot enter than\n3 digits or more than the\nlimit of the buttons!",
            size_hint = [0.6 , 0.20], pos_hint= {'center_x':0.5, 'center_y':0.50}, auto_dismiss = False,
            buttons = [
                MDIconButton(
                    icon= "close-box-multiple-outline",
                    size_hint_y = 0.8,
                    size_hint_x = 0.8,
                    theme_text_color= "Custom",
                    text_color= [25, 0, 0, 1],
                    pos_hint= {'center_x':0.98, 'center_y':.6},
                    on_release = self.cardClose)
            ])
        self.my_dialog.open()

    def cardClose(self, obj):
        self.my_dialog.dismiss()

    def button9(self, user, word, site):
        a = self.ids.container
        a.clear_widgets()

        bb = user
        c = self.ids.user
        c.text = ''
        c.clear_widgets()

        d = self.ids.site
        d.text = ''
        d.clear_widgets()

        ss, list,bingo, alpha, char = [],[],{'a':'A','b':'B','c':'c'.upper(),'d':'d'.upper(),'f':'f'.upper(),'e':'e'.upper(),'g':'g'.upper(),'k':'k'.upper(),'h':'h'.upper(),'l':'l'.upper(),'m':'m'.upper(),'n':'n'.upper(),'o':'o'.upper(),'p':'p'.upper(),'q':'q'.upper(),'x':'x'.upper(),'w':'w'.upper(),'z':'z'.upper(),'s':'s'.upper(),'r':'r'.upper(),'t':'T','y':'Y','u':"U",'i':"I"}, ['a'.upper(),'b'.upper(),'s'.upper(),'f'.upper(),'p'.upper()], ['!','@',"#","%",'&','.','£','¢']
        if len(word) == 0:
           for i,x in bingo.items():  
            f = ran(1,3)
            ff = ran(1,5)
            test = f'{char[ff+2]}{alpha[f]}{ran(2,7+1)-1}{i}{ran(0,4+1)}{x}{ran(0,5)}{ran(1,5)}{char[f+1]}'.replace('A',"4").replace('E',"3")
            ss.append(test)
            ss.sort(reverse=True)

        elif len(word)== 3:
            for i,x in bingo.items():
                f =ran(0,4)
                ff = ran(1,5)
                test = f'{char[ff+2]}{alpha[f]}{word}{x}{ran(0,6)}{i}{ran(1,6)}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{x}{word}{ran(1,6)}{char[ff+2]}{alpha[f]}{ran(0,8+1)}{char[f-2]}'
                test3 = f'{word.capitalize()}{ran(1,6)}{char[f-1]}{alpha[f]}{ran(0,8+1)}{char[f-2]}'
                test4 = f'{ran(1,6)}{char[f-1]}{alpha[f]}{x}{char[f-2]}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                ss.sort(reverse=True)
                
        elif len(word)== 4:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{alpha[f]}{word}{x}{ran(0,6)}{ran(1,6)}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{x}{word}{ran(1,6)}{char[f-1]}{alpha[f]}{char[f-2]}'
                test3 = f'{word.capitalize()}{ran(1,6)}{i}{alpha[f]}{ran(0,8+1)}{char[f-2]}'
                test4 = f'{ran(1,6)}{char[f-1]}{alpha[f]}{ran(0,8+1)}{i}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                ss.sort(reverse=True)    
               
        elif len(word)== 5:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{i}{char[f-1]}{alpha[f]}{word}{ran(1,8+1)}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{x}{word}{ran(1,6)}{i}{char[f-2]}'
                test3 = f'{word.capitalize()}{i}{alpha[f]}{ran(0,8+1)}{char[f-2]}'
                test4 = f'{char[f-1]}{alpha[f]}{ran(0,8+1)}{i}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                ss.sort(reverse=True)
                                               
        elif len(word)== 6:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{alpha[f]}{word}{ran(1,8+1)}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{word}{ran(1,6)}{i}{char[f-2]}'
                test3 = f'{word.capitalize()}{i}{ran(0,8+1)}{char[f-2]}'
                test4 = f'{char[f-1]}{alpha[f]}{i}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                ss.sort(reverse=True)
                                    
        elif len(word)== 7:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{x}{word}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{word}{x}{char[f-2]}'
                test3 = f'{word.capitalize()}{i}{char[f-2]}'
                test4 = f'{char[f-1]}{i}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                ss.sort(reverse=True)
                   
        elif len(word)== 8:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{word}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{word}{char[f-2]}'
                test3 = f'{word.capitalize()}{char[f-2]}'
                test4 = f'{char[f-1]}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                ss.sort(reverse=True)
                 
        else:
            if len(word) == 1:
                self.openCard()
            
            elif len(word) == 2:
                self.openCard()
            
            else:
                if len(word) >= 9:
                    self.openCard()

        for item in ss[0:5]:
            list.append(item)
        for b in ss[40:50]:
            list.append(b)
        for c in ss[80:90]:
            list.append(c)
        for d in ss[6:11]:
            list.append(d)
        list.sort(reverse=True)
        
        for i in list:
            text1, secondaryText, tertiaryText = i, bb, site
           
            if len(secondaryText) == len(tertiaryText) == 0:
                secondaryText ='User not informed'
                tertiaryText = 'Site not informed'
                test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                a.add_widget(test_Three_Text_List_Item1)
                test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)
            else:
                if len(secondaryText) == 0:
                    secondaryText ='User not informed'
                    test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                    a.add_widget(test_Three_Text_List_Item1)
                    test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)

                elif len(tertiaryText) == 0:
                    tertiaryText ='Site not informed'
                    test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                    a.add_widget(test_Three_Text_List_Item1)
                    test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)

                else:
                    if len(secondaryText) != 0:
                        test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                        a.add_widget(test_Three_Text_List_Item1)
                        test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)

                    elif len(tertiaryText) != 0:
                        test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                        a.add_widget(test_Three_Text_List_Item1)
                        test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)
        
        list, ss, bb =[],[], ''

    def button6(self, user, word, site):
        a = self.ids.container
        a.clear_widgets()

        bb = user
        c = self.ids.user
        c.text = ''
        c.clear_widgets()

        d = self.ids.site
        d.text = ''
        d.clear_widgets()
        
        ss, list, bingo, alpha, char = [],[],{'a':'A','b':'B','c':'c'.upper(),'d':'d'.upper(),'f':'f'.upper(),'e':'e'.upper(),'g':'g'.upper(),'k':'k'.upper(),'h':'h'.upper(),'l':'l'.upper(),'m':'m'.upper(),'n':'n'.upper(),'o':'o'.upper(),'p':'p'.upper(),'q':'q'.upper(),'x':'x'.upper(),'w':'w'.upper(),'z':'z'.upper(),'s':'s'.upper(),'r':'r'.upper(),'t':'T','y':'Y','u':"U",'i':"I"}, ['a'.upper(),'b'.upper(),'s'.upper(),'f'.upper(),'p'.upper()], ['!','@',"#","%",'&','.','£','¢']
        if len(word) == 0:
            for i,x in bingo.items():
                f = ran(1,3)
                ff = ran(1,5)
                test = f'{f-2+1}{f+3}{ran(1,8+1)}{alpha[f-1]}{i}{char[ff+2]}'.replace('A',"4").replace('O',"0")
                ss.append(test)
                ss.sort(reverse=True)

        if len(word)== 3:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{word}{x}{ran(0,7)}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{x}{word}{alpha[f]}{char[f-2]}'
                test3 = f'{word.capitalize()}{ran(0,6)}{char[f-1]}{alpha[f]}'
                test4 = f'{ran(1,6)}{alpha[f]}{char[f-2]}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                            
        elif len(word)== 4:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{word}{x}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{i}{word}{char[f-1]}'
                test3 = f'{word.capitalize()}{ran(1,6)}{alpha[f]}'
                test4 = f'{char[f-1]}{i}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                                        
        elif len(word)== 5:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{word}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{x}{word}'
                test3 = f'{word.capitalize()}{i}{char[f-2]}'
                test4 = f'{ran(0,8+1)}{word.capitalize()}'
                ss.append(test3)
                ss.append(test)
                ss.append(test4)
                ss.append(test2)
                ss.sort(reverse=True)
                
        else:
                if len(word) == 1:
                    self.openCard()
                
                elif len(word) == 2:
                    self.openCard()
                
                else:
                    if len(word) >= 6:
                        self.openCard()
      
        for item in ss[0:9]:
            item = item.replace("9","p").replace("3","E").replace("o","0").replace("a","4").replace("2","9")
            list.append(item)
        for b in ss[45:55]:
            b = b.replace("9","p").replace("o","0").replace("a","4")
            list.append(b)
        for c in ss[80:90]:
            c = c.replace("9","p").replace("3","E").replace("o","0")
            list.append(c)
        for d in ss[10:20]:
            d = d.replace("9","p").replace("o","0").replace("a","4")
            list.append(d)
        list.sort(reverse=True)
        
        for i in list:
            text1, secondaryText, tertiaryText = i, bb, site

            if len(secondaryText) == len(tertiaryText) == 0:
                    secondaryText ='User not informed'
                    tertiaryText = 'Site not informed'
                    test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                    a.add_widget(test_Three_Text_List_Item1)
                    test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)
            else:
                if len(secondaryText) == 0:
                    secondaryText ='User not informed'
                    test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                    a.add_widget(test_Three_Text_List_Item1)
                    test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)

                elif len(tertiaryText) == 0:
                    tertiaryText ='Site not informed'
                    test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                    a.add_widget(test_Three_Text_List_Item1)
                    test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)

                else:
                    if len(secondaryText) != 0:
                        test_Three_Text_List_Item1 = MDThreeLineAvatarIconListItem1()
                        a.add_widget(test_Three_Text_List_Item1)
                        test_Three_Text_List_Item1.test(text1, secondaryText, tertiaryText)
                        
        list, ss, bb =[],[], ''
 
class App_principal(md_application):
    
    def build(self):
        App_principal.title = "Capivara_Password"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = '500'
        app_layout= bd.load_string(box2)
        return app_layout

    def check_1(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'BlueGray'
            self.theme_cls.primary_hue = '50'
            
        else:
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.primary_palette = "BlueGray"
            self.theme_cls.primary_hue = '500'
                
if __name__ == '__main__':
    project = App_principal()
    project.run()
