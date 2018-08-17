import tkinter
from  tkinter import ttk

win = tkinter.Tk()
win.title("button按钮控件")
win.geometry("600x200+300+300")

# 创建表格控件
table = ttk.Treeview(win)

# 设置表头
table["columns"] = ("name","age","address")
# 设置每一列的宽度
table.column("name",width = 100)
table.column("age",width = 100)
table.column("address",width = 100)
# 给表头设置值
table.heading("name",text="姓名/name")
table.heading("age",text="年龄/age")
table.heading("address",text="地址/address")

# 插入数据
table.insert("",1,text="line1",value=("奥巴马",65,"华盛顿"))
table.insert("",2,text="line2",value=("普京",60,"莫斯科"))
table.insert("",2,text="line3",value=("莫迪",68,"新德里"))


table.pack()
win.mainloop()








