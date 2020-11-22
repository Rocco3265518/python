import time

status_dict ={
    "username":'',
    "status": False
}


def auth(f):
    '''

    :return:
    '''
    def inner(*args,**kwargs):
        if status_dict['status']:
            ret = f(*args,**kwargs)
            return ret
        else:
            username = input('请输入用户名').strip()
            password = input('请输入密码').strip()
            if username == 'xiaohei' and password == '123':
                print('登录成功')
                status_dict['username'] = username
                status_dict['status'] = True
                ret = f(*args, **kwargs)
                return ret
            else:
                print('登录失败')
    return inner



@auth
def articile():
    print('欢迎访问文章页面')


@auth
def comment():
    print('欢迎访问评论页面')


@auth
def photo():
    print('欢迎访问图片页面')


articile()
comment()
photo()