'''
num = 1
while num <= 100:

    if num == 38:
        print("你是38号")
        break   #跳出该整个循环
    print("执行了",num)
    num += 1
'''

num = 0
while num <= 100:
    num += 1
    if num == 38: #如果在第一个条件中找到了, 则不继续寻找 ,     则需要跳出本次循环
        print("你是38号")
        continue #跳出本次循环

    print(num)






