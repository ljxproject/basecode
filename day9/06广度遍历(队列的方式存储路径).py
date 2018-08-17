import os
import collections

# 深度遍历目录,获取该目录下的所有的目录名和文件名
def getAllDirAndFile(path):
    # 创建一个空的列表
    queue = collections.deque()
    # 向队列中添加第一个路径
    queue.append(path)

    while True:
        # 如果队列中没有了路径,则终止循环
        if len(queue) == 0:
            break

        #   取出需要遍历的目录
        dealPath = queue.popleft()

        listFileName = os.listdir(dealPath)
        for  fileName in listFileName:
        #   拼接绝对路径
            absPath = os.path.join(dealPath,fileName)
            if os.path.isdir(absPath):
                print("目录:%s"%(fileName))
            #   添加到队列中去
                queue.append(absPath)
            if os.path.isfile(absPath):
                print("文件:%s"%(fileName))


path = r"E:\pythondemo\bj1707"
# path = r"I:\bj1707"
getAllDirAndFile(path)


























