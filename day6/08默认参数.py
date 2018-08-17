# def printNameAgeHeigth(name,age,sex = "男",heigth):
# 设置默认值得参数需要放在参数列表的最后面
def printNameAgeHeigth(name,age,heigth = 150,sex = "男"):
    # pass
    print("name=%s,age = %d,heigth = %d,sex = %s"%(name,age,heigth,sex))

printNameAgeHeigth("金三胖子",30,150,"男")
# python中设置了默认参数后,该默认参数可以不传递,可以替换掉默认值
printNameAgeHeigth("金三胖子",30,80)
printNameAgeHeigth("金三胖子",30)






















