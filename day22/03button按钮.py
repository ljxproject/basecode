
import tkinter

win = tkinter.Tk()
win.title("button按钮控件")
win.geometry("300x300+300+300")

# def func():
#     print("别摸我脚Y子")
def func(name):
    print("别摸%s脚Y子"%(name))


# 创建一个button
# command用来指定点击按钮后调用的函数
# btn = tkinter.Button(win,text="登陆",width=7,bg="#ffcccc",command=func)

#
# func1 = lambda :func("余钟炜")
# 通过lambda传值
# btn = tkinter.Button(win,text="登陆",width=7,bg="#ffcccc",command=lambda :func("余钟炜"))

# 退出
btn = tkinter.Button(win,text="登陆",width=7,bg="#ffcccc",command=win.quit)



# 显示
btn.pack()




win.mainloop()









