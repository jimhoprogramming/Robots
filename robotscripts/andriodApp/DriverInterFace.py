from abc import ABCMeta,abstractmethod,abstractproperty

class DriverInterFace:       #python 3 Ҫ�� class DriverInterFace(metaclass=ABCMeta) ��������ʽ�������
    __metaclass__=ABCMeta    #python 2
                                        
    #�ڳ�ʼ��ʱ����ʵ�ֵ�ʵ��
    def __init__(self��Engine,LightCtrl,ForntView,Steeringwheel,SpeedBox):
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

    #���������������ʵ�ֵķ���--���󷽷�    
    @abc.abstractmethod
    def Drive(self):
        pass
    #ͬ��
    @abc.abstractmethod
    def SetInterFace(self):
        pass
    
    
