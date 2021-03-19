from flask import Blueprint

# 可以通过url_prefix参数给蓝图定义的路由添加统一的URL资源段前缀
home = Blueprint('home', __name__, url_prefix='/home')

__import__('home.views')

def go():
    print("gooo...")

# 蓝图也可以设置请求钩子 只有访问该蓝图定义的路由时才会触发局部监听
@home.before_request
def before_request_go():
    print('home before_request_go')