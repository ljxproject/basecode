import pymongo


# 连接mongo服务器
# host 主机名
# port 端口号
connec = pymongo.MongoClient(host="localhost",port=27017)

# 使用数据库
# connect后面跟需要使用的数据库名字, 如果这个名字不存在,会自动创建新
db = connec.myclass

#使用集合
# db后面需要使用的集合名.
collect = db.student

collect.update({"name":"王五"},{"$set":{"age":38}},multi=True,upsert=True)

# 关闭连接
connec.close()