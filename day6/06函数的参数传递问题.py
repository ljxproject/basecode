
# 传递不可变类型,   number,string,tuple...
def editNumber(num):
    # num = num1 = 100
    print(id(num))
    num = 10000
    print(id(num))
    print(num)

num1 = 100
print(id(num1))
editNumber(num1)
print(num1)


# 传递可变类型的参数 , list,dict
def editListNumber(listNum):
    listNum[0] = 250
    print(listNum[0])
    print(id(listNum))


listN = [1,2,3,4]
editListNumber(listN)
print(listN)
print(id(listN))





























