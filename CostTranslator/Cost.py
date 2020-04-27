'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-24 22:06:54
@LastEditors: Mar Ping
@LastEditTime: 2020-04-25 10:37:57
''
import win32con
import win32api

win32api.keybd_event(91, 0, 0, 0)  # win键位码是91
win32api.keybd_event(16, 0, 0, 0)  # shift键位码是16
win32api.keybd_event(83, 0, 0, 0)  # s键位码是83
win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
'''
'''
import win32ui
dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
dlg.SetOFNInitialDir('C:\\Users\\Desktop')  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName()  # 获取选择的文件路径和名称</pre>
'''
'''
from PIL import ImageGrab
image = ImageGrab.grabclipboard()  # 获取剪贴板文件
'''
import PyHook3
from PIL import ImageGrab,Image
import win32con
import win32api
import Hook

def cost():
    win32api.keybd_event(91, 0, 0, 0)  # win键位码是91
    win32api.keybd_event(16, 0, 0, 0)  # shift键位码是16
    win32api.keybd_event(83, 0, 0, 0)  # s键位码是83
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
    return True

if cost() == True:
    Hook.open_mouse()
    if Hook.mouse_state == True:
        print("ok")
        image = ImageGrab.grabclipboard()  # 获取剪贴板文件
        print("done")
        image.show()
        Hook.close_mouse()
