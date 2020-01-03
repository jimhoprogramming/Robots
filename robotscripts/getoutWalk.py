import sys
import function1_ctrlJpg
##import Function1_nn_getTheata


#1调用图片学习,得到以地面识别为主的theata
def function1():
##    function1_ctrlJpg.setY()
    Y=function1_ctrlJpg.getY()                                  #定义Y阵代表各种物品索引号.以文件形式保存备用
    for i in range(len(Y)):
        jpegSourceUrl=Y['SaveURL']
        size=[20,20]
        YID=Y['TID']
        savetoUrl=None
        XY=function1_ctrlJpg.getXY(jpegSourceUrl,size,YID,savetoUrl)   #把单个20X20的图片(从原始160X120快照上截取)排成一行矢量的X阵.以文件形式保存备用
    #调用神经网络计算取得分类器theata

function1()
#2调用新图片载入准备识别区域








#3调用sliding windows 比较每块的性质并用色块标定









#4调用人工控制记录模块状建立一组行为对应关系.循环1处,自动生成多组图片-行为对应关系.









#5调用机器学习,由4一段时间生成的数据得到一组theta.准备为即时的3生成一组即时的控制行为.









#用5的theta用3的图象得到控制信号控制机器运动.









#停止行进




















