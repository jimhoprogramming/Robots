import wx

class ToggleButtons(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(300, 200))
       
        self.colour = wx.Colour(0, 0, 0)
       
        wx.ToggleButton(self, 1, 'red', (20, 25))
        wx.ToggleButton(self, 2, 'green', (20, 65))
        wx.ToggleButton(self, 3, 'blue', (20, 105))
       
        self.panel = wx.Panel(self, -1, (150, 20), (110, 110), style=wx.SUNKEN_BORDER)
        self.panel.SetBackgroundColour(self.colour)
       
        self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed, id=1)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleGreen, id=2)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleBlue, id=3)
       
        self.Center()
        self.ShowModal()
        self.Destroy()
       
    def ToggleRed(self, event):
        green = self.colour.Green()
        blue = self.colour.Blue()
        if self.colour.Red():
            self.colour.Set(0, green, blue)
        else:
            self.colour.Set(255, green, blue)
        self.panel.SetBackgroundColour(self.colour)

    def ToggleGreen(self, event):
        red = self.colour.Red()
        blue = self.colour.Blue()
        if self.colour.Green():
            self.colour.Set(red, 0, blue)
        else:
            self.colour.Set(red, 255, blue)
        self.panel.SetBackgroundColour(self.colour)
       
    def ToggleBlue(self, event):
        red = self.colour.Red()
        green = self.colour.Blue()
        if self.colour.Blue():
            self.colour.Set(red, green, 0)
        else:
            self.colour.Set(red, green, 255)
        self.panel.SetBackgroundColour(self.colour)
       
app = wx.App(0)
ToggleButtons(None, -1, 'togglebuttons.py')
app.MainLoop()
