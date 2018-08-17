import redis


r = redis.Redis()

d1 = {

    "three":{"name":"xxx",
            "count":1,},
    "four":{"name":"yyy",
            "count":2,}
}

r.hset("root","times2",d1)
print(r.hgetall("root"))