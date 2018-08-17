import time
'''
时间: UTC协调时间,格林威治天文时间 ,世界统一时间,世界标准时间.    UTC+8(北京时间,快8个小时)  表示东北区
      DST(夏令时),是为了节约能源而人为规定的的时间, 夏季快一小时

# 时间的表现形式
1.时间戳
    以整型或者浮点型来表示一个时间间隔,   是以 1970年1月1日,0点0分0秒 为参考时间

2.时间元组
   一种python的数据结构表示,  这个元组有9个整型内容
年   tm_year
月   tm_month  0-11   1-12
日   tm_day

时
分
秒

一个星期中的第几天
一年中的第几天
是否是夏令时  tm_isdst   0是   1 不是    -1自己处理

3.字符串形式
  例: 2017/10/16    2017-10-16 10:16:09        20171016    会有多种形式
%a  本地（locale）简化星期名称
%A  本地完整星期名称
%b  本地简化月份名称
%B  本地完整月份名称
%c  本地相应的日期和时间表示
%d  一个月中的第几天（01 - 31）
%H  一天中的第几个小时（24小时制，00 - 23）
%I  第几个小时（12小时制，01 - 12）
%j  一年中的第几天（001 - 366）
%m  月份（01 - 12）
%M  分钟数（00 - 59）
%p  本地am或者pm的相应符
%S  秒（01 - 61）
%U  一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周
%w  一个星期中的第几天（0 - 6，0是星期天）
%W  和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x  本地相应日期
%X  本地相应时间
%y  去掉世纪的年份（00 - 99）
%Y  完整的年份
%Z  时区的名字（如果不存在为空字符）
%%  ‘%’字符





'''

# 获取当前的时间戳 ,以秒为单位
time1 = time.time()
print(time1)

# 时间戳转换为时间元组
# gmtime是获取世界标准时间, 如果没有参数,表示将当前的世界标准时间转换成时间元组
tupleTime1 = time.gmtime()
# tupleTime1 = time.gmtime(time1)
print(tupleTime1)

# 获取本地时间(UTC+8),   如果没有参数,表示将当前本地时间转换成时间元组
tupleTime2 = time.localtime()
# tupleTime2 = time.localtime(time1)
#将 时间戳 转换成时间
# tupleTime2 = time.localtime(1470614888)
print(tupleTime2)

# 时间元组转换成时间戳, 不能为空参, 会自动舍弃时间戳小数部分
time2 = time.mktime(tupleTime2)
print(time2)

# 将时间元组转换成时间字符串
# 需求1:  转换成  2017-10-18 11:38:05   格式:  %Y-%m-%D %H:%M:%S
# 参数1:时间格式
# 参数2: 时间元组
# strTime = time.strftime("%Y-%m-%d %H:%M:%S",tupleTime2)
# 中文的格式
strTime = time.strftime("%Y{y}%m{m}%d{d}  %H:%M",tupleTime2).format(y="年",m="月",d="日")


# 简写方式
# time.strftime("%X %x",time.localtime())
print(strTime)

# 将时间字符串转换成时间元组
# 参数1:  时间字符串
# 参数2:  时间格式字符串,时间格式必须与时间字符串格式对应
tupleTime3 = time.strptime("2017-10-18 11:38:05","%Y-%m-%d %H:%M:%S")
print(tupleTime3)

# 将时间戳转换成字符串
strTime3 = time.ctime(time.time())
print(strTime3)

# 将时间元组转换成字符串
strTime4 =  time.asctime(time.localtime())
print(strTime4)


# 让程序睡一会, 参数是  休眠多长时间 , 单位是秒
# 此处是故意睡眠,客服给钱后,在进行优化
print("开始睡眠")
# time.sleep(2)
print("睡醒了")


#记录该程序cpu的执行时间
#在window系统中, 第一次执行clock表示的记录当前开始的时间, 下次执行clock表示的是与上次执行clock的执行时间间隔
clock1 = time.clock()
print(clock1)
# 模拟
time.sleep(2)
clock2 = time.clock()
print(clock2)
clock3 = time.clock()
time.sleep(2)
print(clock3)










































