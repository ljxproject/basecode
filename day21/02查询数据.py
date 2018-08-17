import pymongo
from bson.objectid import ObjectId

# 连接服务器
conn = pymongo.MongoClient(host="localhost",port=27017)
# 获取数据
db = conn.myclass
# 获取集合
collect = db.student

# 查询所有的数据,并显示出来
# ress = collect.find()
# print(ress)
# # 结果是cursor对象,可以遍历
# print(type(ress))
#
# # 可以遍历,
# # 每条数据是一个字典
# for i in ress:
#     print(i)
#     print(type(i))
#     print(i.get("name"))

# 条件查询
# ress = collect.find({"age":{"$gt":18,"$lt":20}},{"name":1,"age":1})
# for i in ress:
#     print(i)

# 根据_id查询
# ress = collect.find({"_id":ObjectId("5a3a0683b6e77f1cec312e59")})
# for  i in ress:
#     print(i)

# 排序
# 默认是升序
# ress = collect.find().sort("age")
# 降序
# ress = collect.find().sort("age",pymongo.DESCENDING)
# for i in ress:
#     print(i)

# 分页:
ress = collect.find().skip(1).limit(2)
for i in ress:
    print(i)


conn.close()




