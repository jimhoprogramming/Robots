from abc import ABCMeta,abstractmethod,abstractproperty

class DriverInterFace:       #python 3 要用 class DriverInterFace(metaclass=ABCMeta) 这样的形式定义基类
    __metaclass__=ABCMeta    #python 2
                                        
    #在初始化时引入实现的实例
    def __init__(self，Engine,LightCtrl,ForntView,Steeringwheel,SpeedBox):
        if not isinstance(Engin,DriverInterFace):
            raise TypeError('Expected object of type DriverInterFace,got{}'.format(type(Engine).__name__))
        self.__Engine=Engine
        if not isinstance(LightCtrl,DriverInterFace):
            raise TypeError('Expected object of type DriverInterFace,got{}'.format(type(LightCtrl).__name__))
        self.__LightCtrl=LightCtrl
        if not isinstance(FrontView,DriverInterFace):
            raise TypeError('Expected object of type DriverInterFace,got{}'.format(type(FrontView).__name__))
        self.__FrontView=frontView
        if not isinstance(Steeringwheel,DriverInterFace):
            raise TypeError('Expected object of type DriverInterFace,got{}'.format(type(Steeringwheel).__name__))
        self.__Engine=Steeringwheel
        if not isinstance(SpeedBox,DriverInterFace):
            raise TypeError('Expected object of type DriverInterFace,got{}'.format(type(SpeedBox).__name__))
        self.__SpeedBox=SpeedBox

    #定义必须在子类中实现的方法--抽象方法    
    @abc.abstractmethod
    def Drive(self):
        pass
    #同上
    @abc.abstractmethod
    def SetInterFace(self):
        pass
    
    
