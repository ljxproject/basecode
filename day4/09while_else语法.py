'''
格式：
while 表达式１：　
    语句１
    break
else :
    语句２
描述：　循环ｗｈｉｌｅ会判断表达式１，如果为真则执行循环体，
　　　当表达式１为假时，会跳出循环体，执行ｅｌｓｅ中的语句２
'''

# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# print("结束")

listP = ["钱七","赵六","王五","李四","张三"]
# s = None
i = 0
while i < len(listP):
    if "王五" == listP[i]:
        # s = "王五"
        print("已经找到了")
        break
    i += 1
else:
    print("没有找到")
# if s == None:
#     print("没有找到")
# 描述:  当while循环遇到break关键字终止该循环后不会执行else



















