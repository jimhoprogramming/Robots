#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

class LoginScreen(FloatLayout):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        #self.cols=3
        #self.rows=3
        
        self.add_widget( IconButton1 (text='pic here',size_hint=(0.2,0.2),pos_hint={'x':0,'y':0.4}))
        self.add_widget( IconButton2 (text='normal button 1', size_hint=(0.2,0.2),pos_hint={'x':0.117,'y':0.4}))
        self.add_widget( IconButton3 (text='normal button 2', size_hint=(0.2,0.2),pos_hint={'x':0.233,'y':0.4}))
        self.add_widget( IconButton4 (text='normal button 3', size_hint=(0.2,0.2),pos_hint={'x':0,'y':0.2}))
        #self.add_widget( Button (text='normal button 4', size_hint=(0.2,0.2),pos_hint={'x':0.12,'y':0.2}))
        self.add_widget( IconButton6 (text='normal button 5', size_hint=(0.2,0.2),pos_hint={'x':0.233,'y':0.2}))
        self.add_widget( IconButton7 (text='normal button 6', size_hint=(0.2,0.2),pos_hint={'x':0,'y':0}))
        self.add_widget( IconButton8 (text='normal button 7', size_hint=(0.2,0.2),pos_hint={'x':0.117,'y':0}))
        self.add_widget( IconButton9 (text='normal button 8', size_hint=(0.2,0.2),pos_hint={'x':0.233,'y':0}))
        
class IconButton1(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton1,self).__init__(**kwargs)
        self.source='ull.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='ulaa.jpg'
    def on_release(self):
        self.source='ull.jpg'
        
class IconButton2(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton2,self).__init__(**kwargs)
        self.source='us.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='usa.jpg'
    def on_release(self):
        self.source='us.jpg'

class IconButton3(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton3,self).__init__(**kwargs)
        self.source='ur.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='ura.jpg'
    def on_release(self):
        self.source='ur.jpg'

class IconButton4(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton4,self).__init__(**kwargs)
        self.source='ls.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='lsa.jpg'
    def on_release(self):
        self.source='ls.jpg'

class IconButton5(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton5,self).__init__(**kwargs)
        self.source='ull.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='ulaa.jpg'
    def on_release(self):
        self.source='ull.jpg'

class IconButton6(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton6,self).__init__(**kwargs)
        self.source='rs.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='rsa.jpg'
    def on_release(self):
        self.source='rs.jpg'
        
class IconButton7(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton7,self).__init__(**kwargs)
        self.source='dl.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='dla.jpg'
    def on_release(self):
        self.source='dl.jpg'

class IconButton8(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton8,self).__init__(**kwargs)
        self.source='ds.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='dsa.jpg'
    def on_release(self):
        self.source='ds.jpg'
        
class IconButton9(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton9,self).__init__(**kwargs)
        self.source='dr.jpg'
    def on_press(self):
        print('i am IconButtom on_press')
        self.source='dra.jpg'
    def on_release(self):
        self.source='dr.jpg'
        
        
        
class TestApp(App):
        
    def build(self):        
        # display a button with the text : Hello QPython 
        #return IconButton(text='Hello QPython')
        return LoginScreen()
        
if __name__ =='__main__':
    TestApp().run()

