#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from CarElements import ThreeButtomSteeringwheel

class CarDriverBroad(FloatLayout):
    def __init__(self,**kwargs):
        super(CarDriverBroad,self).__init__(**kwargs)
        #加入一个三按钮方向盘实例
        self.add_widget( ThreeButtomSteeringwheel(text='pic here',size_hint=(0.2,0.2),pos_hint={'x':0,'y':0.4}))
        #加入一个前进\停止\倒行\调速\档位器实例
        #self.add_widget( IconButton2 (text='normal button 1', size_hint=(0.2,0.2),pos_hint={'x':0.117,'y':0.4}))
        #加入开关钥匙实例
        #self.add_widget( IconButton3 (text='normal button 2', size_hint=(0.2,0.2),pos_hint={'x':0.233,'y':0.4}))                
        #加入前挡风玻璃显示面板实例
        
class TestApp(App):    
    def build(self):        
        # display a button with the text : Hello QPython 
        #return IconButton(text='Hello QPython')
        return CarDriverBroad()
    
if __name__ =='__main__':
    TestApp().run()

