"""
字符串的定义:  用 单引号 '  '或者" "包裹起来的就是字符串
"""
# 字符串的常见操作(运算)

# 拼接
name = "wen"
age  =  17
sex  =  "纯爷们"
mess = name +  "是一个" + sex
# mess2 = name +  "今年芳龄" + 17  python中字符串不能直接与 数字直接拼接
mess2 = name +  "今年芳龄" + str(age)
print(mess)
print(mess2)

#  乘法操作
mess3 = mess2 * 10
print(mess3)




























