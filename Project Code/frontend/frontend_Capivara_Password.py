tamaño_patalla = (400,600)

box = '''

<Tela1>: 
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
            row_default_height: 250
            adaptive_height: True
        
            FloatLayout:

                MDLabel:
                    text: "1st step:".title()
                    font_size: 21
                    size_hint_x: 0.9
                    pos_hint: {'center_x':0.46, 'center_y':0.99}
                    width:200
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    
                MDTextField:
                    id: user
                    font_size: 18
                    size_hint_x: 0.9
                    hint_text: str('User:')
                    pos_hint: {'center_x':0.5, 'center_y':0.79}
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
                    pos_hint: {'center_x':0.5, 'center_y':0.60}
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

                MDLabel:
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
                
                MDLabel:
                    text: "2st step:".title()
                    font_size: 21
                    size_hint_x: 0.9
                    pos_hint: {'center_x':0.46, 'center_y':0.002}
                    width:200
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    
                MDCard:
                
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
            
<MDThreeLineListItem1>:

<MDThreeLineAvatarIconListItem1>:
    IconRightWidget:
        icon: 'plus-box-multiple'
        on_release:
            root.buttonTest()

<ContentNavigationDrawer>

    ScrollView:
        do_scroll_x: False
        do_scroll_y: True

        MDList:

            OneLineListItem:
                text: " generate password".title().center(25)
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "tela1"

            OneLineListItem:
                text: "saved passwords".title().center(25)
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "tela2"

MDScreen:   
    BoxLayout:

        orientation: 'vertical'

        MDToolbar:
            
            id:'bar2'
            title: "Capivara_Password"
            size_hint_y:0.11
            elevation:20
            opacity: .99
            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
        
        MDNavigationLayout:
            #x: toolbar.height 

            ScreenManager: 
                id: screen_manager

                Tela1:
                    name: 'tela1'

                Tela2:
                    name: 'tela2'

            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
    

             
'''

