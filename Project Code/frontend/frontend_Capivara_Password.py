Tamaño_patalla = (400,600)

box = '''

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
            row_default_height: 270
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
            row_default_height: 270
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
                    helper_text: str('find your passwords').center(5).title()
                    helper_text_mode: "on_focus"
                    multiline: False

                MDRoundFlatIconButton:
                    id: button
                    icon: "magnify"
                    text: "Let's Search"
                    font_size: 15.5
                    pos_hint: {'center_x':0.766, 'center_y':0.55} 
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
                text: 'Alpha Version 0.3.0'
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

            Image:
                id: image
                source: 'test3.png'
                #allow_stretch: True
                size_hint: .3, .3
                pos_hint: {'center_x':0.5, 'center_y':0.83}
                radius: [35, 35, 35, 35, 35]

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
                text: 'Alpha Version 0.3.0'
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
