from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# 1. 创建API对象  用于管理类视图(资源)
api = Api(app)


# 2.定义类视图  继承Resource
class DemoResource(Resource):
    def get(self):
        # 类视图响应的content-type默认变为json形式
        # 类视图的可以直接返回字典
        return {'foo': 'get'}

    def post(self):
        return {'foo': 'post'}

    def put(self):
        return {'foo': 'put'}


# 3.添加类视图
api.add_resource(DemoResource, '/index')

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)