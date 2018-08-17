# 队列数据结构
#  [1,2,3,4,5]
# 集合 双向列表
import collections

# 创建一个空的双向集合
queue =  collections.deque()
# 添加元素,append会将该元素添加到集合的右侧
queue.append("A")
print(queue)
queue.append("B")
print(queue)

# 将元素添加到集合的左侧
# queue.appendleft("C")
# print(queue)

queue.append("C")
queue.append("D")
print(queue)



# 取  先进先出的方式取, pop是从集合右侧开始取
# res1 = queue.pop()
# print(res1)
# print(type(res1))

# 从左侧取
res1  = queue.popleft()
print(res1)
print(queue)

res2  = queue.popleft()
print(res2)
print(queue)

































