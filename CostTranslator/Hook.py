'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-25 01:18:27
@LastEditors: Mar Ping
@LastEditTime: 2020-04-25 20:45:01
'''
import PyHook3
import win32api

mouse_state = False
hm = PyHook3.HookManager()

# 鼠标事件处理函数
def OnMouseEvent(event):
    
    print('MessageName:', event.MessageName)  # 事件名称
    print('Message:', event.Message)  # windows消息常量
    print('Time:', event.Time)  # 事件发生的时间戳
    print('Window:', event.Window)  # 窗口句柄
    print('WindowName:', event.WindowName)  # 窗口标题
    print('Position:', event.Position)  # 事件发生时相对于整个屏幕的坐标
    print('Wheel:', event.Wheel)  # 鼠标滚轮
    print('Injected:', event.Injected)  # 判断这个事件是否由程序方式生成，而不是正常的人为触发。
    print('---')
    global mouse_state
    if str(event.MessageName) == 'mouse left up':
        mouse_state = True
        if str(event.Message) == '514':
            print(mouse_state)
            win32api.PostQuitMessage()
    # 返回True代表将事件继续传给其他句柄，为False则停止传递，即被拦截
    return True

# 将OnMouseEvent函数绑定到 MouseLeftUp 事件上
hm.MouseLeftUp = OnMouseEvent


hm.HookMouse()  # 设置鼠标钩子

hm.UnhookMouse()  # 取消鼠标钩子
mouse_state = False

