import sys
import function1_ctrlJpg
##import Function1_nn_getTheata


#1����ͼƬѧϰ,�õ��Ե���ʶ��Ϊ����theata
def function1():
##    function1_ctrlJpg.setY()
    Y=function1_ctrlJpg.getY()                                  #����Y����������Ʒ������.���ļ���ʽ���汸��
    for i in range(len(Y)):
        jpegSourceUrl=Y['SaveURL']
        size=[20,20]
        YID=Y['TID']
        savetoUrl=None
        XY=function1_ctrlJpg.getXY(jpegSourceUrl,size,YID,savetoUrl)   #�ѵ���20X20��ͼƬ(��ԭʼ160X120�����Ͻ�ȡ)�ų�һ��ʸ����X��.���ļ���ʽ���汸��
    #�������������ȡ�÷�����theata

function1()
#2������ͼƬ����׼��ʶ������








#3����sliding windows �Ƚ�ÿ������ʲ���ɫ��궨









#4�����˹����Ƽ�¼ģ��״����һ����Ϊ��Ӧ��ϵ.ѭ��1��,�Զ����ɶ���ͼƬ-��Ϊ��Ӧ��ϵ.









#5���û���ѧϰ,��4һ��ʱ�����ɵ����ݵõ�һ��theta.׼��Ϊ��ʱ��3����һ�鼴ʱ�Ŀ�����Ϊ.









#��5��theta��3��ͼ��õ������źſ��ƻ����˶�.









#ֹͣ�н�




















