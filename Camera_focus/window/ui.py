from tkinter import *
from tkinter import messagebox


class Application(Frame):


    def __init__(self, master=None):
        super().__init__(master)    # super()父类定义
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """"创建组件"""
        self.btn0l = Button(self)
        self.btn0l["text"] = "自动对焦"
        self.btn0l.pack()
        self.btn0l["command"] = self.自动对焦


        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

        # 显示图像
        global photo  # 把photo声明全局变量
        photo = PhotoImage(file="imgs/logo.png")
        self.labe02 = Label(self, image=photo)
        self.labe02.pack()

        self.labe03 = Label(self, text="银川能源学院\n银智团队", borderwidth=5, relief="solid", justify="right")
        self.labe03.pack()



    def 自动对焦(self):
        messagebox.showinfo("程序正在运行...")


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300+600+600")
    root.title("camera")
    app = Application(master=root)
    root.mainloop()