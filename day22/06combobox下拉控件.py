import tkinter
from  tkinter import ttk

win = tkinter.Tk()
win.title("button按钮控件")
win.geometry("300x300+300+300")

# 创建一个下拉框控件
combox = ttk.Combobox(win)
# 给下拉控件设置值(多个)
combox["values"] = ("北京","上海","深圳","广州","杭州")

# 设置默认选中值
# 参数写 索引
combox.current(2)

# 获取当前的值
# res = combox.get()
# print(res)

def func(event):
    print(combox.get())
# 绑定事件
combox.bind("<<ComboboxSelected>>",func)


# 显示
combox.pack()


win.mainloop()







