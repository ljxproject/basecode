#创建并显示窗口
import tkinter

win = tkinter.Tk()
win.title("Label标签")
win.geometry("300x300+300+300")

# 创建label标签
# 参数1表示的就是父容器, 就是窗口win
# text 指定的是文本内容
# height 指定的是标签的高度, 单位约是字符的高度
# weidth 指定标签的宽度,
# bg  指定背景色
# fg  指定字体颜色
# font 设置字体,和大小


label = tkinter.Label(win,text="金三胖胖 is  a  good man",
                      width=6,height = 1,bg="#ffcccc",
                      fg="#ff0000",font=("宋体",30)
                      )
# 显示label
label.pack()

win.mainloop()





