from flask import Flask, Response

app = Flask(__name__)


# 每次执行视图函数之前调用, 对请求进行一些准备处理, 如参数解析, 黑名单过滤, 数据统计等
@app.before_request
def before_request_1():
    print('before_request 1')


@app.before_request
def before_request_2():
    print('before_request 2')


# 每次执行视图函数之后(已经包装为响应对象)调用, 对响应进行一些加工处理, 如设置统一响应头, 设置数据的外层包装
@app.after_request
def after_request_1(response):  # 必须定义形参接收响应对象
    print('after_request_1')
    return response


@app.after_request
def after_request_2(response):
    print('after_request_2')
    return response


# web应用被第一次请求前调用, 可以进行web应用初始化处理, 如数据库连接
@app.before_first_request
def before_first_request():
    print('before_first_request')


# 每次执行视图函数之后调用, 无论是否出现异常都会执行, 一般用于请求收尾, 如资源回收, 异常统计
@app.teardown_request  # 测试时不要开启调试模式
def teardown_request(error):  # 必须定义形参来接收具体错误信息, 如果没有错误, error=None
    print('teardown_request : %s' % error)


@app.route('/hook')
def hook():
    print('执行视图')
    return "index"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

