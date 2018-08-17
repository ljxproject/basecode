# 导入模块
import functools

# 将字符串转换成10进制数据
# print(int("10"))
# 有多个  二进制字符串转换成十进制
# base的默认值是 10
print(int("1010",base=2))
print(int("101010",base=2))
# 想 int("10100")  直接转

# 重新定义函数
def intB(num):
    return  int(num,base=2)

print(intB("1010"))


# 偏函数
# 参数1: 需要转变的函数名,参数2:需要设置的默认参数
int2 = functools.partial(int,base=2)
print(int2("10101"))



















