'''
for循环: for循环可以方便的循环处理序列类型的数据 ,比如 字符串, 列表
格式:
for 变量   in  序列类型的数据 :
    语句

描述：for循环，会将序列类型数据中的每一个元素挨个取出来，并赋值给变量，直到序列类型数据取完为止

'''
list1 = ["a",2,"b",4,5]
# for n in list1:
#     print(n)

for  i in range(len(list1)):
    print(list1[i])

#rang([start,]stop[,step])

for index,n in enumerate(list1):
    print("%d=%s"%(index,n))

# str2 = "wen is a good man"
# for s in str2:
#     print(s)





































