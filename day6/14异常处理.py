# 概述: 让程序遇到问题时不让程序结束,而越过错误继续向下执行
# 作用:   用来检测try语句块中的错误，从而让except语句捕获错误信息并处理
'''
 格式:
try:
   语句块(可能会出现异常的代码块)
except 错误码1 as e:
    处理1
except 错误码2 as e:
    处理2
else: 可有可无
   当没有异常的时候会调用


格式:
try:
   语句块(可能会出现异常的代码块)
except 错误码1 as e:
    处理1
except 错误码2 as e:
    处理2
finally: 最终的
   始终会执行
........


'''
# 会报ZeroDivisionError错误
# num = 5/0



try:
   # num = 5/0
   print(b)
   # print("没有异常")
# except:  #可以匹配所有类型的错误
#     print("出现了错误")
except  ZeroDivisionError as e:
     print("除数不能为0错误")
except NameError as e:
    print("变量名异常")
finally:
    print("finally")


# else:
#     print("else")

print("try外部")






















