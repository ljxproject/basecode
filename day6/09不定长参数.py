# 不定长参数: 处理能比定义时更多的参数

#加了*的变量, 用来表示没有命名的多个变量,会自动的将这些没有命名的变量封装成一个元组,传递进来
# 如果函数调用时没有传递变量,则是一个空元组
# 可变长度参数最好放在参数列表的最后面,


# 需求: 求n个数的和
# 定义普通函数:  def addMoreNum(num1,num2,num3,num4,......)
# 定义不定长函数:
def addMoreNum(name,*args):
   print(name)
   print(args)
   print(type(args))
   for num in args:
       print(num)


# 调用
# addMoreNum(12,23,34)
# addMoreNum(23)
# addMoreNum()
# addMoreNum(12,23,"胖子")  会报错
# addMoreNum(12,23,name = "胖子")
# addMoreNum("胖子",12,23)

addMoreNum(12,23,34)


# # 例: 求任意多个数的和
# def addMoreNUM(*args):
#     count = 0
#     for num in args:
#         count += num
#     return  count
#
#
# print(addMoreNUM(12,12,23,89,10))


# 加了 ** 的变量, 代表键值对的多个参数的列表, 与*类似, 会自动的将多个 带变量的参数 自动的封装成一个字典,参数名作为key,参数值作为value
# 如果函数调用时没有传递键值对,则是一个空字典
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for  key in  kwargs:
        print(key,kwargs[key])


# 调用
# func("胖子",18,180) 不可用
# func(name = "胖子",age = 18,weight = 180)
func(name = "胖子",age = 18,weight = 180)
func()

# 结构
def function(*args,**kwargs):
    pass

function(89,90,name = "胖子",age = 89)

















































