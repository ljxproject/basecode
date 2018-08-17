import tkinter
from  tkinter import ttk

win = tkinter.Tk()
win.title("button按钮控件")
win.geometry("300x300+300+300")

def getLikes():
    # print("1")
    # 获取选中的爱好
    likesList = []
    if va1.get() == True:  #money被选中
        likesList.append("money")
    if va2.get() == True:
        likesList.append("power")
    if va3.get()  == True:
        likesList.append("beautifulgirl")

    print(likesList)

va1 = tkinter.BooleanVar()
va2 = tkinter.BooleanVar()
va3 = tkinter.BooleanVar()


# 创建多个Checkbutton
cb1 = ttk.Checkbutton(win,text="money",variable = va1,command=getLikes)
cb2 = ttk.Checkbutton(win,text="power",variable = va2,command=getLikes)
cb3 = ttk.Checkbutton(win,text="beautifulgirl",variable = va3,command=getLikes)

cb1.pack()
cb2.pack()
cb3.pack()
win.mainloop()






