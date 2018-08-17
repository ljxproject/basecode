#创建并显示窗口
import tkinter

win = tkinter.Tk()
win.title("Label标签")
win.geometry("300x300+300+300")

#<Button-1>鼠标左键
#<Button-3>鼠标右键
#<Button-2>鼠标中键
#<Double-Button-1>鼠标左键双击
#<Double-Button-3>鼠标右键双击
#<Double-Button-2>鼠标中键双击
#<Triple-Button-1>鼠标左键三击
#<Triple-Button-3>鼠标右键三击
#<Triple-Button-2>鼠标中键三击



btn = tkinter.Button(win,text="点我Y",width=7,bg="#ffcccc")
btn.pack()

# event 就是鼠标事件, 包含鼠标的操作信息
def func(event):
    print("触发了鼠标右键")
    print("x:%d,y:%d"%(event.x,event.y))

# 给btn 绑定一个鼠标右键
# btn.bind("<Button-3>",func)
btn.bind("<Double-Button-1>",func)

win.mainloop()




