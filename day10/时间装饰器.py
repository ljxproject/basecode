import time

def decorator_time(func):
    def iner(*args,**kwargs):
        time.clock()
        func(*args,**kwargs)
        cost_time = time.clock()
        print(cost_time)
    return iner


@decorator_time
def test_dt(num):
    for i in range(num):
        pass


test_dt(1000000000)
