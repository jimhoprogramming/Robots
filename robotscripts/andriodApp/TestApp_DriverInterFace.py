#test_DriverInterFace_main
def main():
    #自己名=基类构造器名(子类名)-----方式生成使用实例
    myDriverInterFace=DriverInterFace(HumenDriverInterFace())
    #表面调用实例中的某个必须实现的方法,实质调用接口里的不同功能但这里被隔离了.
    myDriverInterFace.SetInterFace()
    
    
    
