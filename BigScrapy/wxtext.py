# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
@author:LiWei
@license:LiWei
@contact:877129310@qq.com
@version:
@var:
@note:

"""
import random
import time
from threading import Thread

import wx


class my_frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 200))
        panel = wx.Panel(self)
        Gs = wx.GridSizer(2, 2, 1, 1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 温度值
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lable1 = wx.StaticText(panel, -1, "温度：")
        hbox1.Add(lable1, 0, wx.ALL, 10)
        self.temperature = wx.TextCtrl(panel)
        hbox1.Add(self.temperature, 1, wx.ALL, 10)
        Gs.Add(hbox1)

        # PM2.5
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        lable2 = wx.StaticText(panel, -1, "PM2.5：")
        hbox2.Add(lable2, 0, wx.ALL, 10)
        self.PM2 = wx.TextCtrl(panel)
        hbox2.Add(self.PM2, 1, wx.ALL, 10)
        Gs.Add(hbox2)

        # 湿度
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        lable3 = wx.StaticText(panel, -1, "湿度：")
        hbox3.Add(lable3, 0, wx.ALL, 10)
        self.humidity = wx.TextCtrl(panel)
        hbox3.Add(self.humidity, 1, wx.ALL, 10)
        Gs.Add(hbox3)

        panel.SetSizer(Gs)
        self.Centre()
        self.Show(True)
        self.Fit()


class TestThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        while 1:
            time.sleep(1)
            frame.temperature.SetValue("%s°" % (str(random.randint(-10, 45))))
            frame.PM2.SetValue("%s" % (str(random.randint(50, 500))))
            frame.humidity.SetValue("%s%%" % (str(random.randint(10, 95))))


app = wx.App()
frame = my_frame(None, u'动态显示-wxpython')
TestThread()
app.MainLoop()
