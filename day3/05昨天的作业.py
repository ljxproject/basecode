'''
1.彩票系统:用户输入一个数,再随机生成一个数,判断2个数是否相等,如果相等,恭喜中奖了\

2.从控制台输入一个三位数，如果是水仙花数(是指一个三位数,其各位数字立方和等于该数 )就打印“是水仙花数”，否则打印“不是水仙花数”
153=1^3+5^3+3^3


3.从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
11111   12321   12221

4.
#不准使用max min
从控制台输入两个数，输出较大的值

从控制台输入三个数，输出较大的值
'''


# 水仙花数
num  = int(input("请输入一个３位数"))
# 153
num1 = num//100
num2 = num%100//10
num3 = num%10

if num == num1**3 + num2**3 + num3**3:
    print("这是水仙花数")
else:
    print("他是假的")


# 判断三个数的大小
max = None
num4 = 23
num5 =12
num6 =45
num7 = 12

if  num4 > num5:
    max = num4
else:
    max = num5

if max < num6:
    max = num6



















