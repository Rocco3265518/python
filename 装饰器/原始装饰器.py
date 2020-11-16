import time

def index():
    '''很多代码'''
    time.sleep(2)
    print('欢迎登陆我的博客')


def timmer(f):
    def inner():
        startime = time.time()
        f()
        endtime = time.time()
        print(f'测试本函数执行效率{endtime - startime}')
    return  inner


index = timmer(index)
index()