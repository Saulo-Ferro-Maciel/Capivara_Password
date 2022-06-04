from box2 import*
from random import randint as ran

from kivy.lang import Builder as bd # cria o metódo construir 
from kivy.core.window import Window as tamaño_pantalla # regula o tamanho da janela
from kivy.uix.screenmanager import Screen # tela
from kivy.properties import StringProperty

from kivymd.app import MDApp as md_application # cria a janela
from kivymd.uix.boxlayout import MDBoxLayout as Box
from kivymd.uix.floatlayout import FloatLayout as Float
from kivymd.uix.list import IconRightWidget as icon_Rigth
from kivymd.uix.list import ThreeLineAvatarIconListItem as three_Line_List
from kivymd.uix.list import ThreeLineListItem as three_Line_List2


tamaño_pantalla.size = tamaño_patalla

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

class AlertaCard(Float):
    
    def close(self):
        
        self.parent.remove_widget(self) 

class NavigationDrawer(Box):
    pass

class Tela1(Screen):

    def widgetUpdate(self):
        test_Text_List_Item1 = MDThreeLineListItem1()
        self.ids.container.add_widget(test_Text_List_Item1)
        test_Text_List_Item1.test()
    
        self.ids.user.clear_widgets()
        self.ids.word.clear_widgets()
      
        self.ids.word.text = str("")
        self.ids.user.text = str('')

        self.ids.user.disabled = True
        self.ids.word.disabled = True
        self.ids.container.disabled = True

    def closeCard(self):

        self.ids.user.disabled = False
        self.ids.word.disabled = False
        self.ids.container.disabled = False
          
    def openCard(self):

        self.widgetUpdate()

        a = self.add_widget(AlertaCard())

    def button9(self, user, word):
        a = self.ids.container
        a.clear_widgets()

        bb = user
        c = self.ids.user
        c.text = ''
        c.clear_widgets()

        ss, list,bingo, alpha, char = [],[],{'a':'A','b':'B','c':'c'.upper(),'d':'d'.upper(),'f':'f'.upper(),'e':'e'.upper(),'g':'g'.upper(),'k':'k'.upper(),'h':'h'.upper(),'l':'l'.upper(),'m':'m'.upper(),'n':'n'.upper(),'o':'o'.upper(),'p':'p'.upper(),'q':'q'.upper(),'x':'x'.upper(),'w':'w'.upper(),'z':'z'.upper(),'s':'s'.upper(),'r':'r'.upper(),'t':'T','y':'Y','u':"U",'i':"I"}, ['a'.upper(),'b'.upper(),'s'.upper(),'f'.upper(),'p'.upper()], ['!','@',"#","%",'&','.','£','¢']
        if len(word) == 0:
           for i,x in bingo.items():
            for s in char:
                d , f = s,ran(0,4)
                test = f'{char[f-2+1]}{alpha[f]}{ran(2,7+1)-1}{i}{ran(0,4+1)}{x}{ran(0,5)}{ran(1,5)}{d}'.replace('A',"4").replace('E',"3")
                ss.append(test)
                ss.sort(reverse=True)

        elif len(word)== 3:
            for i,x in bingo.items():
                f =ran(0,4)
                test = f'{char[f-1]}{alpha[f]}{word}{x}{ran(0,6)}{i}{ran(1,6)}'.replace('A',"4").replace('E',"3").replace("S","&").replace("I","1").replace('a',"@").replace("s","$")
                test2 = f'{x}{word}{ran(1,6)}{char[f-1]}{alpha[f]}{ran(0,8+1)}{char[f-2]}'
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
            text1, secondaryText = i, bb
            if len(secondaryText) == 0:
                secondaryText ='User not informed'
                textos = three_Line_List(text=text1, secondary_text=secondaryText)
                textos.add_widget(icon_Rigth(icon='plus-box-multiple'))
                a.add_widget(textos)
                
            else:
                if len(secondaryText) != 0:
                    textos = three_Line_List(text=text1, secondary_text=secondaryText)
                    textos.add_widget(icon_Rigth(icon='plus-box-multiple'))
                    a.add_widget(textos)
        
        list, ss, bb, textos =[],[], '', ''

    def button6(self, user, word):
        a = self.ids.container
        a.clear_widgets()

        bb = user
        c = self.ids.user
        c.text = ''
        c.clear_widgets()
        
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
            text1, secondaryText = i, bb
            if len(secondaryText) == 0:
                secondaryText ='User not informed'
                textos = three_Line_List(text=text1, secondary_text=secondaryText)
                textos.add_widget(icon_Rigth(icon='plus-box-multiple'))
                a.add_widget(textos)
                
            else:
                if len(secondaryText) != 0:
                    textos = three_Line_List(text=text1, secondary_text=secondaryText)
                    textos.add_widget(icon_Rigth(icon='plus-box-multiple'))
                    a.add_widget(textos)
        
        list, ss, bb, textos =[],[], '', ''
 
class App_principal(md_application):
    
    def build(self):
        App_principal.title = "Capivara_Password"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = '500'
        app_layout= bd.load_string(box)
        return app_layout
           
if __name__ == '__main__':
    project = App_principal()
    project.run()
