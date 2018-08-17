'''
递归: 一个函数调用自身的编程技称为递归
     循环能做的事情,递归也能做

思维方式:
    1.找出这一次调用和上一次的关系
    2.找出临界条件
    3.假设当前的函数已经能够使用,调用自身求出上一次结果,再求出本次结果
'''


# 例:   计算 1 + 2 + 3  + 4 .......+n

# count = 0
# for i in range(1,101):
#    count += i
# print(count)

n = 0
count = 0
while n <= 100:
    count += n
    n += 1




'''
1 + 2  + 3 + 4 +5 ....
sum(1)  + 2 +3 + 4 + 5
sum(2) + 3 + 4 + 5
sum(3) + 4 + 5
sum(4)  + 5
sum(5)


sum(5) = sum(4)    + 5
sum(4) = sum(3) + 4
sum(3) = sum(2) + 3
sum(2) = sum(1)  + 2


sum(1) = 1

'''

# 定义递归函数
def  sum(n):
    # 找到出口
    if n == 1:
        return  1
    return sum(n-1) + n


print(sum(100))























