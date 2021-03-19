from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def deco1(f):
    def wrapper(*args, **kwargs):
        print('deco1')
        return f(*args, **kwargs)

    return wrapper


def deco2(f):
    def wrapper(*args, **kwargs):
        print('deco2')
        return f(*args, **kwargs)

    return wrapper


class DemoResource(Resource):
    # 通过method_decorators类属性来设置类视图的装饰器
    # method_decorators = [deco1, deco2]  # 列表形式 所有请求方式都会使用
    method_decorators = {'get': [deco1, deco2], 'post': [deco2]}  # 字典形式 给请求方式分别设置装饰器

    # @deco1
    # @deco2
    def get(self):
        return {'foo': "get"}

    def post(self):
        return {'foo': "post"}


# 3.添加类视图
api.add_resource(DemoResource, '/index')

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)
