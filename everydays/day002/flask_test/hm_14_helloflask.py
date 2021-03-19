from flask import Flask
from flask_restful import Resource, Api, marshal, fields, marshal_with

app = Flask(__name__)
api = Api(app)


class User:  # 定义模型类
    def __init__(self):
        self.name = 'zs'
        self.age = 20
        self.height = 1.8
        self.scores = [80, 90]
        self.info = {
            'gender': True
        }

    # 添加转换为字典的方法
    def to_dict(self):
        return {
            'name': 'zs',
            'age': 20,
            'height': 1.8,
            'scores': [80, 90],
            'info': {'gender': True},
        }


fields = {  # 序列化规则
    'username': fields.String(attribute='name'),  # 指定对应的模型属性
    'age': fields.Integer(default=10),  # 设置默认值
    'height': fields.Float,
    'scores': fields.List(fields.Integer),  # 元素类型唯一
    'info': fields.Nested({'gender': fields.Boolean})
}


class DemoResource(Resource):

    method_decorators = {'post': [marshal_with(fields, envelope='post_data')]}

    def get(self):
        user = User()
        # marshal函数可以按照指定的序列化规则将模型对象转为字典
        return marshal(user, fields)
        # envelope 指定转换后的 json 数据嵌套在哪一个 key 下
        # return marshal(user, fields, envelope='data')

    def post(self):
        # 只需要返回模型对象
        return User()

    def put(self):
        # 调用模型自身的方法返回字典
        user = User()
        return user.to_dict()


api.add_resource(DemoResource, '/response')

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)