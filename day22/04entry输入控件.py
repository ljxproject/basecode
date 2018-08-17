
import tkinter

win = tkinter.Tk()
win.title("button按钮控件")
win.geometry("300x300+300+300")


variable = tkinter.Variable()
# 创建一个输入控件
entry = tkinter.Entry(win,textvariable = variable)

# 设置输入框中的字符串
variable.set("余钟炜是个啥")
# 获取输入框中输入的字符串
res = variable.get()
print(res)

# 显示
entry.pack()

win.mainloop()

