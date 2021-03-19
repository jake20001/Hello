from flask import Flask, g, current_app

app = Flask(__name__)


@app.route('/index')
def index():
    # 打印当前 app 的信息
    print(current_app)
    print(current_app.__dict__)
    print(current_app.url_map)
    return 'index'


@app.route('/g')
def g_context():
    # 设置 name 属性
    g.name = "zhangsan"
    return 'g'


@app.route('/g2')
def g_context_2():
    # 这里是另外一个请求，g 被重置，没有了 name 属性
    print(hasattr(g, 'name'))
    return 'g2'


if __name__ == '__main__':
    # 只能在请求范围内使用，这里会报错
    # print(current_app)
    # print(g)
    app.run(host='0.0.0.0', port=5000, debug=True)