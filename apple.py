#! /usr/bin/env python

""" Test octoFLU initial page
This is a test
"""

import wx
import os
import os.path

class MainFrame(wx.Frame):
    """
    This is a basic frame
    """

    def __init__(self,*args,**kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        pnl = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        vbox=wx.BoxSizer(wx.VERTICAL)

        hbox1=wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(pnl, label="blastn")
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc1=wx.FilePickerCtrl(pnl, wx.ID_ANY, path = wx.EmptyString, message="Select a file",wildcard="*.exe", style=wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL)
        hbox1.Add(tc1,proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,10))

        hbox2=wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(pnl, label="makeblastdb")
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        tc2=wx.FilePickerCtrl(pnl, wx.ID_ANY, path = wx.EmptyString, message="Select a file",wildcard="*.exe", style=wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL)
        hbox2.Add(tc2,proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,10))

        hbox4=wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(pnl, label="FastTree")
        st4.SetFont(font)
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        tc4=wx.FilePickerCtrl(pnl, wx.ID_ANY, path = wx.EmptyString, message="Select a file",wildcard="*.exe", style=wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL)
        hbox4.Add(tc4,proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(pnl, label='Matching Classes')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(pnl, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        vbox.Add((-1, 25))

        #self.Bind(wx.EVT_FILEPICKER_CHANGED, self.onFilePicker, id=self.filePicker.GetId())

        pnl.SetSizer(vbox)

    def onFilePicker(self, event):
        self.resetOnOpen(event)
        path = self.filePicker.GetPath()
        if not os.path.isfile(path):
            return
        self.openFile(event, path)
        self.modifyHistory(event,path)

if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title="Main Frame",size=(600,400))
    frm.Show()
    app.MainLoop()
    
