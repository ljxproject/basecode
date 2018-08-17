import tkinter
from  tkinter import ttk

win = tkinter.Tk()
win.title("button按钮控件")
win.geometry("300x300+300+300")

def func():
    # print("1")
    # pass
    # print(group.get())
    value = group.get()
    if value == 1:
        print("男")
    if  value == 2:
        print("女")
    if value == 3:
        print("不明")

group = tkinter.IntVar()

# 创建radiobutton
radio1 = ttk.Radiobutton(win,text="男",variable = group,value = 1,command = func)
radio2 = ttk.Radiobutton(win,text="女",variable = group,value = 2,command = func)
radio3 = ttk.Radiobutton(win,text="不明",variable= group,value = 3,command = func)
# 显示
radio1.pack()
radio2.pack()
radio3.pack()


win.mainloop()


