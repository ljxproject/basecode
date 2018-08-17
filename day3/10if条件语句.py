'''
格式1:if

语句0
if 表达式:
   语句1;
   语句2....
语句3...
-------------------------------------
格式2:  if - else语句
语句0
if  表达式:
   语句1
   语句2
else:
   语句3
语句4
--------------------------------
格式3:
语句0
if 表达式1:
   语句1
elif 表达式2:
    语句2
elif 表达式3:
    语句3
.....
else:      (除以上情况以外的, 该else可以不写)
   语句4
---------------------------------------------------
格式4:if嵌套
语句1
if 表达式1:
    if 表达式2:
        可以继续嵌套if语句
    else:

    if 表达式3:
    elif
     ....
else:

'''
'''
# 案例1:  if结构
name = "vip"
if "vip" == name:
    print("请走vip通道")
print("上飞机")


# 案例2: if - else
isLike = input("你看我头像牛B吗?")

if isLike == "像":
    print("真像")
else:
    print("不像")
print("....")


# 案例3 : if- elif...else
age = int(input("请输入一个年龄"))

if age < 9 and age >0:
    print("幼儿")
elif age >= 9 and age < 17:
    print("少年")
elif age <= 34:
    print("青年")
elif age <= 59:
    print("中年")
elif age >= 60  and age <= 100:
    print("老年")
else:
    print("你个老妖怪")

#方式2
age = int(input("请输入一个年龄"))
if age < 9 and age >0:
    print("幼儿")

if age >= 9 and age < 17:
    print("少年")

if age <= 34 and  age >=17:
    print("青年")

if age <= 59 and age >= 35:
    print("中年")

if age >= 60  and age <= 100:
    print("老年")

'''

# if嵌套案例
sex = input("请输入性别?")
if sex == "女":
    color = input("你白不白")
    money = input("你有多少钱")
    beautiful = input("你美不美")
    if color == "白" or money > 100 or beautiful == "美":
        print("我们比较适合做朋友")
    elif color == "白" and money > 100 and beautiful == "美":
        print("我们晚上去哪吃饭")
    else:
        print("你是个好人")

else:
    print("我是纯爷们,你走开")






























