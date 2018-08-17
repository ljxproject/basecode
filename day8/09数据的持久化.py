import pickle
# 数据的持久化， 就是将内存中的对象可以保存到文件中去
# 序列化 ----  将对象（变量）保存到文件中去

# names = ["金三胖子","安倍狗","朴槿惠","莫迪","阿三"]
names = ("金三胖子","安倍狗","朴槿惠","莫迪","阿三")

# wf = open("名单.txt","wb")
# # 参数1：需要保存的对象
# # 参数2： 保存文件位置
# pickle.dump(names,wf)
# wf.close()

# 反序列化  ----  将文件中的数据转换成对象（变量）

rf = open("名单.txt","rb")
#参数1:表示文件
data = pickle.load(rf)
print(data)
print(type(data))






















