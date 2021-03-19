from flask import Flask, session, g, abort
from functools import wraps

app = Flask(__name__)

app.secret_key = 'test'


@app.route('/login')
def login():
    """登录"""
    session['username'] = 'zhangsan'
    return '登录成功'


@app.route('/logout')
def logout():
    """退出"""
    if 'username' in session:
        del session['username']
    return '退出成功'


# 需求1: 所有视图都需要获取用户是否已经登录
# 解决办法: 用钩子函数进行封装减少代码冗余
@app.before_request
def set_is_login():
    print('before_request')
    # 使用g变量来传递数据
    if 'username' in session:
        g.is_login = True
    else:
        g.is_login = False


@app.route('/userinfo/')
def user_info():
    # 判段用户是否已经登录
    if g.is_login:
        return 'userinfo'
    abort(401)


def login_required(f):
    def wrapper(*args, **kwargs):
        print("1111111111", f.__name__)
        if g.is_login:
            return f(*args, **kwargs)
        else:
            abort(401)
    return wrapper

# def login_required(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         print("1111111111",wrapper.__name__)
#         if g.is_login:
#             return f(*args, **kwargs)
#         else:
#             abort(401)
#
#     return wrapper

@app.route('/update_password')
@login_required
def update_password():
    return 'update_password'


# @app.route('/update_photo')
# @login_required
# def update_photo():
#     return 'update_photo'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

