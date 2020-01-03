#-*- coding: utf8 -*-
'''
模块名称：GetTrainingSet.py
样本积累部分：
输入为摄像头图像，人工定义代码y
输出为X矩阵，y矩阵
界面使用wxpy。并调用getpic.py模块。即时显示图像，即时定义类别代码。
'''

import wx,os
import getpic


class MainWindow(wx.Frame):
    myudp=None
    image=None
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,400))
        self.CreateStatusBar() # A StatusBar in the bottom of the window
        # Setting up the menu.
        filemenu= wx.Menu()
        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
 
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        #设置摄影、确认、退出的按钮控件
        m_btnCutPic=wx.Button( self,-1, u"拍摄")
        m_btnDefine=wx.Button(self,-1,u"自定义分类对话框")
        m_btnConfirm=wx.Button( self,-1, u"加入训练集")
        m_btnExit=wx.Button(self,-1,u"退出")

        #设置Y分类代码文本框
        


        
        #添加控制面板
        sizerCtrlPanel = wx.BoxSizer(wx.HORIZONTAL)        
        sizerCtrlPanel.Add(m_btnCutPic,1,wx.EXPAND)
        sizerCtrlPanel.Add(m_btnExit,1,wx.EXPAND)
        sizerCtrlPanel.Add(m_btnDefine,1,wx.EXPAND)
        sizerCtrlPanel.Add(m_btnConfirm,1,wx.EXPAND)
        
        #添加摄影后图像的载体面板
        self.ReturnPicPanel=wx.Panel(self,-1)
        self.ReturnPicPanel.SetBackgroundColour(wx.BLACK)
        try:  
            MainWindow.image = wx.Image('d:\\robots\\robotscripts\\data\\OCRData\\tempX.jpg', wx.BITMAP_TYPE_JPEG)  
            temp = MainWindow.image.ConvertToBitmap()  
            size = temp.GetWidth(), temp.GetHeight()  
        except:  
            print("error")
            temp=None
        self.bmp = wx.StaticBitmap(self.ReturnPicPanel,-1,temp,pos=(0, 0),size=size)

        
        #布局整体面板位置
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.ReturnPicPanel,1,flag=wx.EXPAND)
        self.sizer.Add(sizerCtrlPanel,0,flag=wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Centre( wx.BOTH )                

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_BUTTON, self.CutPic,m_btnCutPic)
        self.Bind(wx.EVT_BUTTON, self.ConFirm,m_btnConfirm)
        self.Bind(wx.EVT_BUTTON, self.Define,m_btnDefine)
        self.Bind(wx.EVT_BUTTON, self.OnExit,m_btnExit)

        
        #显示出来
        self.Show(True)

        #设定其他需要用到的局部变量
        
    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets31
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.
 
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def CutPic(self,event):
        myPic=getpic.pic('d:\\robots\\robotscripts\\data\\OCRData','tempX')
        myPic.snapshot()
        MainWindow.image=wx.Image('d:\\robots\\robotscripts\\data\\OCRData\\tempX.jpg', wx.BITMAP_TYPE_JPEG)
        self.bmp.SetBitmap(MainWindow.image.Scale(400, 350).ConvertToBitmap())    
    def ConFirm(self,event):
        pass
    def Define(self,event):
        pass
    
               


 
app = wx.App(False)
frame = MainWindow(None, u"吸尘机建立图像识别训练集程序")
app.MainLoop()
