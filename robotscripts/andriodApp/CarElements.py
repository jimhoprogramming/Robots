#-*-coding:utf8;-*-
#这是一个定义方向盘的类
#qpy:2
#qpy:kivy

#引入需要用到的模块部分
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import abc

#方向盘基类定义
class steeringwheel:
    #------------------------私有变量定义------------------------------
    #'方向','面板图片','位置'
    __direction='f'
    __face=[]
    __posiction=[]
    #------------------------构造函数定义-------------------------------
    def __init__(self):
        #super(steeringwheel,self).__init__(**kwargs)
        #实现面板中3个按钮显示出来公共代码
        self.FaceBroad(self,__face);
        

        
    #---------------------------接口定义--------------------------------
    #子类必须实现不同的输出包括udp发字符\打印文字\显示器       
    @abc.abstractmethod
    def OutputMessage(self):
        pass
        raise NotImplementedError
    #-------------------------定义属性存取------------------------------
    @property
    def face(self):
        return self.__face
    @face.setter
    def face(self,face):
        pass
    #--------------------------公开函数定义-----------------------------
    def FaceBroad(self):
        pass
    def on_press(self):
        print('i am IconButtom on_press')
        self.source=self.__face[2]
    def on_release(self):
        self.source='ull.jpg'
    



    
