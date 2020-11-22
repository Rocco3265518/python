import  time


def timmer(f):
    def inner(*args,**kwargs):
        start_time = time.time()
        ret = f(*args,**kwargs)
        return  ret
    return inner

@timmer
def index(name,age):
    time.sleep(3)
    print(f"欢迎{name},{age}岁光临本网站")



index('小黑',27)

