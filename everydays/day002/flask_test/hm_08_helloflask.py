from flask import Flask, abort

app = Flask(__name__)

# 被装饰的函数需要接受一个参数，用于接收错误对象
# 捕获http错误
@app.errorhandler(405)
def error_404(error):  # 一旦进行捕获, 要求必须定义形参接收具体错误信息
    return f"<h3>您访问的页面去浪迹天涯了</h3> \n {error}"


# 还可以捕获系统内置错误
@app.errorhandler(ZeroDivisionError)
def error_zero(error):
    return f'除数不能为0 \n {error}'


@app.route('/404')
def http_404():
    # 通过 abort 抛出特定的 http 异常
    abort(405)  # 主动抛出异常 (只能抛出http错误)
    return "index"


@app.route('/zero')
def zero():
    a = 1 / 0
    return 'zero'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)