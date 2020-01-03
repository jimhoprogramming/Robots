# -*- coding: cp936 -*-
import time

class Date(object):
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @staticmethod
    def now():
        t=time.localtime()  #返回的当前时间
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    @staticmethod
    def tomorrow():
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    def show(self):
        print'类内变量： %4d %2d %2d' %(self.year,self.month ,self.day)
    @classmethod
    def classshow(cls):
        print'class Date is %4d %2d %2d' %(self.year,self.month,self.day)
    
import abc
 
class A(object):
  __metaclass__ = abc.ABCMeta
 
  @abc.abstractmethod
  def say(self):
    return 'say yeah'
 
  @classmethod
  def __subclasshook__(cls, C):
    if cls is A:
      if any("say" in B.__dict__ for B in C.__mro__):
        return True
    return NotTmplementd
 
class B(object):
  def say(self):
    return 'hello'


if __name__=='__main__':  #主程序
    a=Date(1974,03,16)
    a.show()
    b=Date.now()
    a.show()
    b.show()
    c=Date.tomorrow()
    a.show()
    c.show()
    
