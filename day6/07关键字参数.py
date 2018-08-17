
def printNameAgeHeigth(name,age,heigth):
    # pass
    print("name=%s,age = %d,heigth = %d"%(name,age,heigth))

# 调用
# printNameAgeHeigth("金三胖子",30,150)
# 替换顺序后出错
# printNameAgeHeigth(30,"金三胖子",150)
# printNameAgeHeigth(age = 30,"金三胖子",150)
# python是允许更改传递参数的顺序,但是需要指定 参数名, 参数名错误程序会挂掉
# printNameAgeHeigth(name = "金三胖子",heigth=150,age = 30)










