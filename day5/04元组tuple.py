'''
元组: 是一种有序的集合
特点:  1.与列表list类似
       2.是一种不可变类型
       3.使用小括号

格式:   (元素1,元素2,元素3...)    描述: 元素是以小括号 () 包裹的, 每个元素之间用  ,  分割
'''
# 创建一个空的元组
tuple1 = ()
print(type(tuple1))
print(tuple1)

# 创建一个只有一个元素的元组, 需要加上  ,
tuple2 = (23,)
print(type(tuple2))
print(tuple2)

# 创建一个有多个元素的元组,可以存放不同类型的元素
# tuple3 = (12,23,34,45,56)
tuple4 = (12,23,34,45,56,"ab","cd")
print(tuple4)

# 查 (不可变的类型)
# 查, 可以根据角标来查询数据,  格式:  元组名[角标]
tuple5 = (12,23,34,45,56,"ab","cd")
print(tuple5[2])

# 注意越界异常
# print(tuple5[len(tuple5)])

# 不可以增删改
# 注意: 元组的元素是不可以改变的,如果元组的元素是可变类型,则该元素的子元素可以修改
tuple6 = (12,23,34,45,56,"ab","cd")
# tuple6[2] = 200
tuple7 = (12,23,[22,22,33],45,56,"ab","cd")
# tuple7[2] = 200
tuple7[2][1] = 8888
print(tuple7)

# del tuple7

# 常见的操作
tuple8 = (12,23,34,45,56)
tuple9 = ("12","23","34","45")
# 可以有  +  运算
tuple10 =  tuple8 + tuple9
print(tuple10)
# 可以有  *  运算
print(tuple9*2)

# 成员判断
if 12 in tuple8:
    print("存在")

# 截取操作
tuple11 = (12,23,34,45,56,"12","23","34","45")
print(tuple11[-1])
print(tuple11[::-1])
print(tuple11[1:4])

# 取最大值
tuple12 = (12,23,34,45,56)
print(max(tuple12))
# 取最小值
print(min(tuple12))

# 遍历
# for age in tuple12:
#     print(age)
# for i in range(len(tuple12)):
#     print(tuple12[i])

for index,value  in enumerate(tuple12):
    print(index,value)

# 二维元组
tuple13 = ((12,23,45),("a","bn","hello"),(12,12,12))
print(tuple13)
# 取值
print(tuple13[1][0])

# 三维元组
tuple14 = (((12,23,45),("a","bn","hello"),(12,12,12)),((12,23,45),("a","bn","hello"),(12,12,12)),((12,23,45),("a","bn","hello"),(12,12,12)))
print(tuple14)
print(tuple14[0][1][0])
































































