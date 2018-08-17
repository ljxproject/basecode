
import tkinter

win = tkinter.Tk()
win.title("button按钮控件")
win.geometry("300x300+300+300")

def func():
#     获取输入框中的值
    print(variable.get())

variable = tkinter.StringVar()
entry  = tkinter.Entry(win,textvariable=variable)
button = tkinter.Button(win,text="获取值",width=7,bg="#ffcccc",command=func)
entry.pack()
button.pack()


win.mainloop()







