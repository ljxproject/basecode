#创建并显示窗口
import tkinter

win = tkinter.Tk()
win.title("Label标签")
win.geometry("600x600+300+300")

#
label1 = tkinter.Label(win,text="马克思",width=6,height=2,bg="#800000")
label2 = tkinter.Label(win,text="马巴巴",width=6,height=2,bg="#f0e68c")
label3 = tkinter.Label(win,text="马蓉",width=6,height=2,bg="#00ff00")
label4 = tkinter.Label(win,text="马赛克",width=6,height=2,bg="#5f9ea0")

#绝对布局
# x指定 宽度上的偏移量
# y指定  高度上的偏移量
label1.place(x=100,y=0)
label2.place(x=500,y=0)
label3.place(x=0,y=100)
label4.place(x=100,y=100)




win.mainloop()