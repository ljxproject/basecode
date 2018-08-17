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

# 默认是在中间位置
# label1.pack()

# label2.pack(side=tkinter.TOP)
# label3.pack(side=tkinter.BOTTOM)
# label4.pack(side=tkinter.LEFT)
# label4.pack(side=tkinter.RIGHT)

# label2.pack(side=tkinter.TOP,fill="x")
label2.pack(side=tkinter.LEFT,fill="y")



win.mainloop()





