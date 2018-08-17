'''
打印:
***********
***********
***********
'''
'''
# 第一个循环用来循环行
line = 0
while line < 3:
    # 第二循环用来循环行中的每一个*
    num = 0
    while  num < 10:
        print("*",end="")
        num +=1
    # 换行
    print()
    line +=1
'''


'''
打印:
*
**
***
****
*****
******
*******
'''

line = 0
while line < 10:
    # 第二循环用来循环行中的每一个*
    num = 0
    while  num < line + 1:
        print("*",end="")
        num +=1
    # 换行
    print()
    line +=1









