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

# 向集合中插入 文档
# collect.insert({"name":"张三","age":19,"address":"北京","gender":1})
# 插入多条数据
collect.insert([{"name":"王五","age":28,"address":"深圳","gender":0},{"name":"赵六","age":18,"address":"天津","gender":0},{"name":"hanmeimei","age":22,"address":"广州","gender":0}])


# 关闭连接
connec.close()



