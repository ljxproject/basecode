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

# 表格布局,  column 指定放在哪一列,  row表示放在哪一行
label1.grid(column=1,row=1)
label2.grid(column=2,row=1)
label3.grid(row=2,column=2)


win.mainloop()





