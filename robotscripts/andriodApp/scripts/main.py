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
        self.add_widget( IconButton5 (text='normal button 4', size_hint=(0.2,0.2),pos_hint={'x':0.12,'y':0.2}))

        
class IconButton1(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton1,self).__init__(**kwargs)
        self.source='lsxs.jpg'
    def on_press(self):
        print('i am left on_press')
        IconButton5.source=self.source
    def on_release(self):
        IconButton5.source='usxs.jpg'
        
class IconButton2(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton2,self).__init__(**kwargs)
        self.source='rsxs.jpg'
    def on_press(self):
        print('i am right on_press')
        IconButton5.source=self.source
    def on_release(self):
        IconButton5.source='usxs.jpg'

class IconButton3(ButtonBehavior,Image):
    onoff=True
    def __init__(self,**kwargs):
        super(IconButton3,self).__init__(**kwargs)
        self.source='off.jpg'
        IconButton3.onoff=True
    def on_press(self):
        print('i am IconButtom on_press')
        if IconButton3.onoff:       
            self.source='on.jpg'
            IconButton4.source='red.jpg'
            IconButton5.source='usxs.jpg'
        else:
            IconButton4.source='green.jpg'
            IconButton5.source='offxs.jpg'
            self.source='off.png'
        IconButtom3.onoff=not(IconButton3.onoff)     

class IconButton4(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton4,self).__init__(**kwargs)
        self.source='green.jpg'

class IconButton5(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(IconButton5,self).__init__(**kwargs)
        self.source='offxs.jpg'

        
class TestApp(App):
        
    def build(self):        
        # display a button with the text : Hello QPython 
        #return IconButton(text='Hello QPython')
        return LoginScreen()
        
if __name__ =='__main__':
    TestApp().run()

