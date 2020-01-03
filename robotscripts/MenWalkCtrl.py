#-*- coding: utf8 -*-
#名称：ManWalkCtrl
#此程式目的:实现人工看见图片控制"滚开"前进、后退、左右转向功能。
#输入为图片文件
#输出为udp服务器控制电机代号
#界面使用WXPYTHON完成触摸上下左右按钮、及加速减速滑动条、开机、关停按钮。


import os
import wx
import UdpConnect

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

        #设置方向盘的按钮控件
        m_btnLeft=wx.Button( self,-1, u"←")
        m_btnRight=wx.Button( self,-1, u"→")
        
        #设置车匙上的按钮
        m_btnEngineStart=wx.Button( self,-1, u"引擎开")
        m_btnEngineStop=wx.Button( self,-1, u"熄火")
                
        #添加控制面板
        sizerStreerwheel = wx.BoxSizer(wx.HORIZONTAL)        
        sizerStreerwheel.Add(m_btnLeft,1,wx.EXPAND)
        sizerStreerwheel.Add(m_btnRight,1,wx.EXPAND)

        sizerEngine = wx.BoxSizer( wx.VERTICAL )        
        sizerEngine.Add(m_btnEngineStart,1,wx.EXPAND)
        sizerEngine.Add(m_btnEngineStop,1,wx.EXPAND)        

        sizerCtrl=wx.BoxSizer(wx.HORIZONTAL)
        sizerCtrl.Add(sizerStreerwheel,1,flag=wx.EXPAND)
        sizerCtrl.Add(sizerEngine,0,flag=wx.EXPAND)
        
        #添加挡风玻璃面板的载体面板
        self.panelWindScreen=wx.Panel(self,-1)
        self.panelWindScreen.SetBackgroundColour(wx.BLACK)
        try:  
            MainWindow.image = wx.Image('d:\\robots\\robotscripts\\data\\ground\\g10.jpg', wx.BITMAP_TYPE_JPEG)  
            temp = MainWindow.image.ConvertToBitmap()  
            size = temp.GetWidth(), temp.GetHeight()  
            self.bmp = wx.StaticBitmap(self.panelWindScreen,-1,temp,pos=(0, 0),size=size)  
        except:  
            print("error")
    
        #布局整体面板位置
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panelWindScreen,1,flag=wx.EXPAND)
        self.sizer.Add(sizerCtrl,0,flag=wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Centre( wx.BOTH )                

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_BUTTON, self.PressLeft,m_btnLeft)
        self.Bind(wx.EVT_BUTTON, self.PressRight,m_btnRight)
        self.Bind(wx.EVT_BUTTON, self.PressEngineStart,m_btnEngineStart)
        self.Bind(wx.EVT_BUTTON, self.PressEngineStop,m_btnEngineStop)

        #初始化定时绑定
        self.timer = wx.Timer(self)#创建定时器 
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)#绑定一个定时器事件 


        
        #显示出来
        self.Show(True)

        #设定其他需要用到的局部变量
        #udp_connect=None
        
    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets31
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.
 
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def PressLeft(self,event):
        '''发送udp字符L给滚开wifi的udp服务器端'''
        print MainWindow.myudp.SendCharter('L')

        
    def PressRight(self,event):
        '''发送udp字符R给滚开wifi的udp服务器端'''
        print MainWindow.myudp.SendCharter('R')
        
    def PressEngineStart(self,event):
        '''连接udp服务器并发送udp字符On给滚开wifi的udp服务器端'''
        MainWindow.myudp=UdpConnect.UdpConnect()
        MainWindow.myudp.Connect()
        self.OnStart()

    def PressEngineStop(self,event):
        '''发送udp字符Off给滚开wifi的udp服务器端'''
        self.OnStop()
        MainWindow.myudp.DisConnect()
        
    def getFrontView(self):
        '''每执行一次就向滚开提交取前景拍照的jpeg请求'''
        FileSize,JpegFile=MainWindow.myudp.SendCharter('cammera')
        if FileSize>0:
            print str(FileSize)
            return True,JpegFile
        else:
            print '滚开没有连接或者摄像头相关设备出错。'
            return False,None
    def OnTimer(self, evt):#显示时间事件处理函数
        print 'do OnTimeer Function'
        t,p=self.getFrontView()
        print t
        self.SaveFile(p)
        MainWindow.image=wx.Image('d:\\robots\\robotscripts\\data\\ground\\tempView.jpg', wx.BITMAP_TYPE_JPEG)
        self.bmp.SetBitmap(MainWindow.image.Scale(400, 350).ConvertToBitmap())
        #self.panelWindScreen.Refresh()
    def OnStart(self): 
        self.timer.Start(500)#设定时间间隔为1000毫秒,并启动定时器 
        print 'Have been  OnStart'
    def OnStop(self): 
        self.timer.Stop()
        print 'Have been  OnStop'
    def SaveFile(self,dataLine32):
        myfile=open('d:\\robots\\robotscripts\\data\\ground\\tempView.jpg','wb')
        for c in dataLine32:
            myfile.write(c)
        myfile.close()
 
app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
