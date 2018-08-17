# 导入随机数模块
import  random

# 生成一个随机数,  0 - 10

nums = [0,1,2,3,4,5,6,7,8,9,10]
# 从数据列表中随机选取一个数
num1  = random.choice(nums)
print(num1)

#rang(10) 相当于 [0, 9],rang函数中的参数表示有多少个值,默认从0,开始
num2 = random.choice(range(6,10))
print(num2)

# 随机选取字符串中的一个字符
num3 = random.choice("wenjiabao  is a  good  man")
print(num3)

#生成1-100之间的数
num4 = random.choice(range(100))  +1
print(num4)

#生成随机数
# random.randrange([start,]stop[,step])
# start,生成随机数的起始值,默认起始值是0
# stop, 生成随机数的结束值(不包括该值)
# step ,表示步长,默认步长是1

# num5 = random.randrange(2)
num5 = random.randrange(2,10,3)
print(num5)

nums2 = [0,1,2,3,4,5,6,7,8,9,10]
# 把列表数据重新排列
random.shuffle(nums2)
print(nums2)

# 随机生成一个实数 范围是[0,1]
num6 = random.uniform(0,1)
print(num6)
#生成随机数 ,随机数的范围为[10,12]
print(random.randint(10,12))





























