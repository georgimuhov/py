import os
import sys
import threading
import time
import wx
import wx.adv
import wx.lib.fancytext as fancytext
from wx.adv import TaskBarIcon as TaskBarIcon

try:
    from wx.lib.mswalpha import draw_alpha
except ImportError:
    from mswalpha import draw_alpha


# class MyAboutDlg
# class MyFirstFrame
# class MySecondFrame
# class MyApp

class MyFirstFrame(wx.Frame):
    style = (wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.NO_BORDER |
             wx.FRAME_SHAPED | wx.NO_FULL_REPAINT_ON_RESIZE | wx.STAY_ON_TOP)

    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=style, name='frame'):

        scr_x = int(wx.GetDisplaySize()[0] - 211)
        scr_y = int(wx.GetDisplaySize()[1] - 253)
        pos = (scr_x, scr_y)
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        # Attributes.
        self.hasShape = None
        self.region = None
        self.accel_tbl = None
        self.widgetsframe = None
        self.bitmap = None
        self.normalFont = None
        self.normalBoldFont = None
        self.delta = wx.Point(0, 0)

        # Return application name.
        self.app_name = wx.GetApp().GetAppName()
        # Return bitmaps folder.
        self.bitmaps_dir = wx.GetApp().GetBitmapsDir()
        # Return icons folder.
        self.icons_dir = wx.GetApp().GetIconsDir()

        # Create a timer.
        self.timer = wx.Timer(self)
        self.timer.Start(10000)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        # Simplified init method.
        self.SetProperties()
        self.CreateCtrls()
        self.BindEvents()

    def SetProperties(self):
        self.SetTitle(self.app_name)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        frameIcon = wx.Icon(os.path.join(self.icons_dir, "icon_wx.ico"), type=wx.BITMAP_TYPE_ICO)

        self.SetIcon(frameIcon)

    def CreateCtrls(self):
        # Load a background bitmap.
        self.bitmap = wx.Bitmap(os.path.join(self.bitmaps_dir, "skin.png"), type=wx.BITMAP_TYPE_PNG)

        # or
        # image = wx.Image('skin.png', wx.BITMAP_TYPE_PNG)
        # blurimage = image.Blur(1)
        # self.bitmap = blurimage.ConvertToBitmap()

        self.SetClientSize((self.bitmap.GetWidth(), self.bitmap.GetHeight()))

        if wx.Platform == "__WXGTK__":
            # wxGTK requires that the window be created before you can
            # set its shape, so delay the call to SetWindowShape until
            # this event.
            self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)
        else:
            # On wxMSW and wxMac the window has
            # already been created, so go for it.
            self.SetWindowShape()

        tt = wx.ToolTip('LeftClick to Drag, RightClick to Close!')
        self.SetToolTip(tt)

        # It appears that we cannot make child widgets on the Frame
        # when using mswalpha, therefore we will make a "child" shaped
        # frame that will handle widgets transparency also.
        # self.button = wx.Button(self, -1, 'Button', pos=(100, 100))

        # self.Centre()
        self.widgetsframe = MySecondFrame(self, pos=self.GetPosition(), size=self.GetSize())
        self.widgetsframe.Show()

    def BindEvents(self):
        """
        Bind some events to an events handle.
        """

        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda x: None)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_RIGHT_UP, self.OnExit)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def SetWindowShape(self, *event):
        # Use the bitmap's mask to determine the region.
        self.region = wx.Region(self.bitmap)
        self.hasShape = self.SetShape(self.region)

    def OnLeftDown(self, event):
        if self.HasCapture():
            self.ReleaseMouse()

        self.CaptureMouse()
        x, y = self.ClientToScreen(event.GetPosition())
        originx, originy = self.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = (dx, dy)

    def OnLeftUp(self, event):
        if self.HasCapture():
            self.ReleaseMouse()

    def OnMouseMove(self, event):
        if event.Dragging() and event.LeftIsDown():
            x, y = self.ClientToScreen(event.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.SetPosition(fp)
            self.widgetsframe.SetPosition(fp)

    def Draw(self):
        # Return client size.
        width, height = self.GetClientSize()

        # Return main image size.
        bw, bh = self.bitmap.GetWidth(), self.bitmap.GetHeight()

        dc = wx.MemoryDC()

        fontSize = self.GetFont().GetPointSize()

        # wx.Font(pointSize, family, style, weight, underline, faceName)
        if wx.Platform == "__WXGTK__":
            self.normalBoldFont = wx.Font(fontSize - 1, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, "")
            self.normalFont = wx.Font(fontSize - 2, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, "")
        else:
            self.normalBoldFont = wx.Font(fontSize + 23, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, "")
            self.normalFont = wx.Font(fontSize + 1, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, "")

        # dc.SetFont(self.normalFont)
        # dc.SetFont(self.normalBoldFont)

        bmp = wx.Bitmap.FromRGBA(width, height, red=0, green=0, blue=0, alpha=0)
        dc.SelectObject(bmp)

        gc = wx.GraphicsContext.Create(dc)
        gcdc = wx.GCDC(gc)

        # Draw a bitmap with an alpha channel
        # on top of the last group.
        # image, x, y, transparence
        gcdc.DrawBitmap(self.bitmap, -1, -1, useMask=False)

        # # Draw text.
        # gcdc.SetTextForeground(wx.Colour(80, 80, 80, 255))  # grey
        # gcdc.SetTextBackground(wx.TransparentColour)
        # gcdc.SetFont(self.normalFont)
        # gcdc.DrawText("qxz2uyl", (int(263), int(315)))

        gcdc.Destroy()
        del gcdc

        dc.Destroy()
        del dc

        draw_alpha(self, bmp)

    def OnTimer(self, event):
        dc = wx.BufferedDC(wx.ClientDC(self))
        dc.Clear()

        self.Draw()

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self)
        dc.Clear()

        self.Draw()

    def OnExit(self, event):
        self.widgetsframe.Close()
        self.Close()


class MySecondFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.FRAME_SHAPED | wx.NO_BORDER | wx.FRAME_NO_TASKBAR | wx.FRAME_FLOAT_ON_PARENT,
                 name="frame"):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        # Attributes.
        self.t1 = None
        self.stopper = None
        self.button_minimize = None
        self.button_exit = None
        self.button_pg_admin_terminate = None
        self.button_pg_admin = None
        self.button_start_db = None
        self.button_stop_db = None
        self.button_restart_db = None
        self.delta = None
        self.hasShape = None
        self.region = None
        self.btn1 = None
        self.btn2 = None
        self.SetTransparent(240)

        # Return bitmaps folder.
        self.bitmaps_dir = wx.GetApp().GetBitmapsDir()
        # Return icons folder.
        self.icons_dir = wx.GetApp().GetIconsDir()

        # Simplified init method.
        self.SetProperties()
        self.CreateCtrls()
        self.BindEvents()

    def SetProperties(self):
        self.SetBackgroundColour(wx.BLACK)

    def CreateCtrls(self):

        # Creates the pgAdmin button
        self.button_pg_admin = wx.Button(self, id=-1, label="🐘", pos=(52, 185), size=(28, 25))
        pg_fnt = wx.Font(pointSize=15, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL,
                         weight=wx.FONTWEIGHT_NORMAL)
        self.button_pg_admin.SetFont(pg_fnt)
        self.button_pg_admin.Bind(wx.EVT_BUTTON, self.db_monitoring_func)

        # Creates the Start DB button
        self.button_start_db = wx.Button(self, id=-1, label="▶", pos=(79, 185), size=(28, 25))
        self.button_start_db.Bind(wx.EVT_BUTTON, self.button_start_db_func)

        # Creates the Stop DB button
        self.button_stop_db = wx.Button(self, id=-1, label="■", pos=(106, 185), size=(28, 25))
        self.button_stop_db.Bind(wx.EVT_BUTTON, self.button_stop_db_func)

        # Creates the Restart DB button "🗘" ⟳
        self.button_restart_db = wx.Button(self, id=-1, label="⟳", pos=(133, 185), size=(28, 25))
        restart_fnt = wx.Font(pointSize=18, family=wx.FONTFAMILY_SCRIPT, style=wx.FONTSTYLE_NORMAL,
                              weight=wx.FONTWEIGHT_NORMAL)
        self.button_restart_db.SetFont(restart_fnt)
        self.button_restart_db.Bind(wx.EVT_BUTTON, self.button_restart_db_func)

        # Creates the Minimize button
        self.button_minimize = wx.Button(self, id=-1, label="__", pos=(170, 12), size=(19, 19))
        self.button_minimize.Bind(wx.EVT_BUTTON, self.button_minimize_func)

        # Creates the Exit button
        self.button_exit = wx.Button(self, id=-1, label="X", pos=(190, 12), size=(19, 19))
        self.button_exit.Bind(wx.EVT_BUTTON, self.button_exit_func)

        if wx.Platform == "__WXGTK__":
            # wxGTK requires that the window be created before you can
            # set its shape, so delay the call to SetWindowShape until
            # this event.
            self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)
        else:
            # On wxMSW and wxMac the window has
            # already been created, so go for it.
            self.SetWindowShape()

    def db_monitoring_func(self, event):
        """
        Checks all the time if the Database is alive from slave
        """

        self.t1 = threading.Thread(target=self.db_monitoring_slave_func)
        self.t1.start()

    def db_monitoring_slave_func(self):
        """
        Checks all the time if the Database is alive
        """
        while True:
            path = r"C:\fs_db\pgsql"
            try:
                if path:
                    path = r"C:\fs_db\pgsql"
                else:
                    path = os.path.join(sys.path[0])
            except ImportError as error:
                print(error)
            os.system(rf'cmd /c "{path}\bin\pg_isready.exe -d postgres://localhost:5432/" ')
            time.sleep(1)
            if self.stopper:
                break

    def button_pg_admin_func(self, event):
        """
        Opens the pgAdmin Pandel
        """

        # for p in psutil.process_iter(attrs=['pid', 'name']):
        #     if p.name() != "pgAdmin4.exe":
        #         path = r"C:\fs_db\pgsql"
        #         try:
        #             if path:
        #                 path = r"C:\fs_db\pgsql"
        #             else:
        #                 path = os.path.join(sys.path[0])
        #         except ImportError as error:
        #             print(error)
        #         os.popen(rf'cmd /c "{path}\pgAdmin 4\bin\pgAdmin4.exe" ')
        #     if p.name() == "pgAdmin4.exe":
        #         p.kill()

        path = r"C:\fs_db\pgsql"
        try:
            if path:
                path = r"C:\fs_db\pgsql"
            else:
                path = os.path.join(sys.path[0])
        except ImportError as error:
            print(error)

        os.popen(rf'cmd /c "{path}\pgAdmin 4\bin\pgAdmin4.exe" ')

    def button_start_db_func(self, event):
        """
        Starts a new pgSQL Server
        """

        path = r"C:\fs_db\pgsql"
        try:
            if path:
                path = r"C:\fs_db\pgsql"
            else:
                path = os.path.join(sys.path[0])
        except ImportError as error:
            print(error)

        os.system(rf'cmd /c ""{path}\bin\pg_ctl" -D "{path}\data" -l logfile start" ')

    def button_stop_db_func(self, event):
        """
        Stops the pgSQL Server
        """

        path = r"C:\fs_db\pgsql"
        try:
            if path:
                path = r"C:\fs_db\pgsql"
            else:
                path = os.path.join(sys.path[0])
        except ImportError as error:
            print(error)

        os.system(rf'cmd /c ""{path}\bin\pg_ctl" -D "{path}\data" stop" ')

    def button_restart_db_func(self, event):
        """
        Restarts the pgSQL Server
        """

        path = r"C:\fs_db\pgsql"
        try:
            if path:
                path = r"C:\fs_db\pgsql"
            else:
                path = os.path.join(sys.path[0])
        except ImportError as error:
            print(error)

        os.system(rf'cmd /c ""{path}\bin\pg_ctl.exe" restart -D "{path}\data"" ')

    def button_minimize_func(self, event):
        """
        Minimizes the Program
        """
        pass

    def button_exit_func(self, event):
        """
        Exits the Program
        """

        self.stopper = True
        sys.exit()

    def BindEvents(self):
        """
        Bind some events to an events handler.
        """

        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

    def SetWindowShape(self, *event):
        # Use the widget's rect's to determine the region.
        wxRegion = wx.Region
        self.region = wxRegion()
        widgets = [child for child in self.GetChildren()]
        regions = [wxRegion(widget.GetRect()) for widget in widgets]
        Union = self.region.Union
        [Union(reg) for reg in regions]
        self.hasShape = self.SetShape(self.region)

    def OnLeftDown(self, event):
        if self.HasCapture():
            self.ReleaseMouse()

        self.CaptureMouse()
        x, y = self.ClientToScreen(event.GetPosition())
        originx, originy = self.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = (dx, dy)

    def OnLeftUp(self, event):
        if self.HasCapture():
            self.ReleaseMouse()

    def OnBtnAbout(self, event):
        self.GetParent().OnAbout(self)

    def OnBtnClose(self, event):
        self.GetParent().OnExit(self)

    def OnSlider(self, event):
        self.SetTransparent(event.GetEventObject().GetValue())


class MyApp(wx.App):

    def OnInit(self):
        self.locale = wx.Locale(wx.LANGUAGE_GERMAN)
        self.SetAppName("DB Monitor")
        self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]

        frame = MyFirstFrame(None)
        self.SetTopWindow(frame)
        frame.Show(True)

        return True

    def GetInstallDir(self):
        return self.installDir

    def GetIconsDir(self):
        icons_dir = os.path.join(self.installDir, "icons")
        return icons_dir

    def GetBitmapsDir(self):
        bitmaps_dir = os.path.join(self.installDir, "bitmaps")
        return bitmaps_dir


def main():
    app = MyApp(False)
    app.MainLoop()


if __name__ == "__main__":
    '''
    wxVER = 'wxPython %s' % wx.version()
    pyVER = 'python %d.%d.%d.%s' % sys.version_info[0:4]
    versionInfos = '%s %s' % (wxVER, pyVER)
    print(versionInfos)
    '''
    main()
