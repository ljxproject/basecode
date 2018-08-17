import time
# 解析歌词
musicLrc = """[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
"""
# 目的: 将歌词解析处理
#把歌词解析出来,并用字典保存   key(时间)-value(歌词)
    # 1.把歌词拆分中多行
    # 2.拆分出时间,歌词
    # 3.添加到字典中去

# 拆分多行
listLines = musicLrc.splitlines()
# 创建存放歌词的字典
dictLrc = {}

# 遍历每一行字符串,将每一行字符串拆分成时间,歌词
for line in listLines:
#     [04:40.75] [02:39.90][00:36.25]只是因为在人群中多看了你一眼
#     [04:40.75]  [02:39.90]   [00:36.25]   只是因为在人群中多看了你一眼
#     [04:4075.  ]  [02:39.90    ]   [00:36.25    ]   只是因为在人群中多看了你一眼
#     [04:40.75   [02:39.90      [00:36.25      只是因为在人群中多看了你一眼
      listTimeAndLrc = line.split("]")
      print(listTimeAndLrc)
      # 处理时间,将字符串数据转换成 秒
      for i in range(len(listTimeAndLrc)-1):#取出的是  "[02:23"
         timeStr = listTimeAndLrc[i][1:]  # "02:23"
      #   将分  ,秒   拆开
         timeMH = timeStr.split(":")   #"02"   "23"
      #  转换成浮点型秒
         time =  float(timeMH[0]) * 60 + float(timeMH[1])
         # 将歌词及时间存入到字典
         dictLrc[time] = listTimeAndLrc[-1]

# 字典是无序的
print(dictLrc)
# 通过列表来将key(时间)排序
listTime = []
for time in dictLrc:
    listTime.append(time)
# 将listTime排序,默认是升序
listTime.sort()
print(listTime)

# 按照排序后的时间将歌词取出来
# for t in listTime:
#     print(dictLrc[t])

# 10   歌词1    20  歌词2     30  歌词3    40 歌词4

#
# while True:
#     # 请输入一个时间点
#     setTime = float(input("请输入一个时间点(单位是秒):"))
#     for i in range(len(listTime)):
#         if setTime < listTime[i]:
#     #       取该时间点的上一个时间点对应的歌词
#              lrc =dictLrc[listTime[i-1]]
#              print(lrc)
#              break


while True:
    # 请输入一个时间点
    setTime = 0
    for i in range(len(listTime)):
        if setTime < listTime[i]:
    #       取该时间点的上一个时间点对应的歌词
             lrc =dictLrc[listTime[i-1]]
             print(lrc)
             break
    #      让程序睡1s
    time.sleep(1)
    setTime += 1



































