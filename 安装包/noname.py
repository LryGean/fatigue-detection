# -*- coding: utf-8 -*- 
import wx  # 构造显示界面的GUI
import wx.xrc
import wx.adv

###########################################################################
# Class Fatigue_detecting
##########################################################################

COVER = '../images/camera.png'


class Fatigue_detecting(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition, size=wx.Size(873, 535),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_animCtrl1 = wx.adv.AnimationCtrl(self, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition,
                                                wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE)
        bSizer3.Add(self.m_animCtrl1, 1, wx.ALL | wx.EXPAND, 5)
        bSizer2.Add(bSizer3, 9, wx.EXPAND, 5)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"参数设置"), wx.VERTICAL)
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"视频源"), wx.VERTICAL)
        gSizer1 = wx.GridSizer(0, 2, 0, 8)
        m_choice1Choices = [u"摄像头ID_0", u"摄像头ID_1", u"摄像头ID_2"]
        self.m_choice1 = wx.Choice(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(90, 25),
                                   m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        gSizer1.Add(self.m_choice1, 0, wx.ALL, 5)
        self.camera_button1 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"开始检测", wx.DefaultPosition,
                                        wx.Size(90, 25), 0)
        gSizer1.Add(self.camera_button1, 0, wx.ALL, 5)
        self.vedio_button2 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"打开视频文件", wx.DefaultPosition,
                                       wx.Size(90, 25), 0)
        gSizer1.Add(self.vedio_button2, 0, wx.ALL, 5)

        self.off_button3 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"暂停", wx.DefaultPosition, wx.Size(90, 25),
                                     0)
        gSizer1.Add(self.off_button3, 0, wx.ALL, 5)
        sbSizer2.Add(gSizer1, 1, wx.EXPAND, 5)
        sbSizer1.Add(sbSizer2, 2, wx.EXPAND, 5)
        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"疲劳检测"), wx.VERTICAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.yawn_checkBox1 = wx.CheckBox(sbSizer3.GetStaticBox(), wx.ID_ANY, u"打哈欠检测", wx.Point(-1, -1),
                                          wx.Size(-1, 15), 0)
        self.yawn_checkBox1.SetValue(True)
        bSizer5.Add(self.yawn_checkBox1, 0, wx.ALL, 5)
        self.blink_checkBox2 = wx.CheckBox(sbSizer3.GetStaticBox(), wx.ID_ANY, u"闭眼检测", wx.Point(-1, -1),
                                           wx.Size(-1, 15), 0)
        self.blink_checkBox2.SetValue(True)
        bSizer5.Add(self.blink_checkBox2, 0, wx.ALL, 5)
        sbSizer3.Add(bSizer5, 1, wx.EXPAND, 5)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        self.nod_checkBox7 = wx.CheckBox(sbSizer3.GetStaticBox(), wx.ID_ANY, u"点头检测", wx.Point(-1, -1),
                                         wx.Size(-1, 15), 0)
        self.nod_checkBox7.SetValue(True)
        bSizer6.Add(self.nod_checkBox7, 0, wx.ALL, 5)
        self.m_staticText1 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"疲劳时间(秒):", wx.DefaultPosition,
                                           wx.Size(-1, 15), 0)
        self.m_staticText1.Wrap(-1)
        bSizer6.Add(self.m_staticText1, 0, wx.ALL, 5)
        m_listBox2Choices = [u"3", u"4", u"5", u"6", u"7", u"8"]
        self.m_listBox2 = wx.ListBox(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(50, 24),
                                     m_listBox2Choices, 0)
        bSizer6.Add(self.m_listBox2, 0, 0, 5)
        sbSizer3.Add(bSizer6, 1, wx.EXPAND, 5)
        sbSizer1.Add(sbSizer3, 2, 0, 5)
        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"脱岗检测"), wx.VERTICAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_checkBox4 = wx.CheckBox(sbSizer4.GetStaticBox(), wx.ID_ANY, u"脱岗检测", wx.DefaultPosition,
                                       wx.Size(-1, 15), 0)
        self.m_checkBox4.SetValue(True)
        bSizer8.Add(self.m_checkBox4, 0, wx.ALL, 5)
        self.m_staticText2 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"脱岗时间(秒):", wx.DefaultPosition,
                                           wx.Size(-1, 15), 0)
        self.m_staticText2.Wrap(-1)
        bSizer8.Add(self.m_staticText2, 0, wx.ALL, 5)
        m_listBox21Choices = [u"5", u"10", u"15", u"20", u"25", u"30"]
        self.m_listBox21 = wx.ListBox(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(50, 24),
                                      m_listBox21Choices, 0)
        bSizer8.Add(self.m_listBox21, 0, 0, 5)
        sbSizer4.Add(bSizer8, 1, 0, 5)
        sbSizer1.Add(sbSizer4, 1, 0, 5)
        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"分析区域"), wx.VERTICAL)
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText3 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"检测区域：   ", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer9.Add(self.m_staticText3, 0, wx.ALL, 5)
        m_choice2Choices = [u"全视频检测", u"部分区域选取"]
        self.m_choice2 = wx.Choice(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        bSizer9.Add(self.m_choice2, 0, wx.ALL, 5)
        sbSizer5.Add(bSizer9, 1, wx.EXPAND, 5)
        sbSizer1.Add(sbSizer5, 1, 0, 5)
        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"状态输出"), wx.VERTICAL)
        self.m_textCtrl3 = wx.TextCtrl(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        sbSizer6.Add(self.m_textCtrl3, 1, wx.ALL | wx.EXPAND, 5)
        sbSizer1.Add(sbSizer6, 5, wx.EXPAND, 5)
        bSizer4.Add(sbSizer1, 1, wx.EXPAND, 5)
        bSizer2.Add(bSizer4, 3, wx.EXPAND, 5)
        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # 封面图片
        self.image_cover = wx.Image(COVER, wx.BITMAP_TYPE_ANY)
        # 显示图片在m_animCtrl1上
        self.bmp = wx.StaticBitmap(self.m_animCtrl1, -1, wx.Bitmap(self.image_cover))

        # 设置窗口标题的图标
        self.icon = wx.Icon('../images/123.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        print("wxpython界面初始化加载完成！")


class main_app(wx.App):
    """
     在OnInit() 里边申请Frame类，这样能保证一定是在app后调用，
     这个函数是app执行完自己的__init__函数后就会执行
    """

    # OnInit 方法在主事件循环开始前被wxPython系统调用，是wxpython独有的
    def OnInit(self):
        self.frame = Fatigue_detecting(parent=None, title="Fatigue Demo")
        self.frame.Show(True)
        return True


if __name__ == "__main__":
    app = main_app()
    app.MainLoop()
