from flask import Flask

from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 定义转换器类, 继承BaseConverter
class MyBoolConverter(BaseConverter):
    # 用于对路径参数进行匹配
    regex = "([0nNFf]|[1yYTt])"


    true_values = "1yYTt"
    false_values = "0nNFf"

    # 对路径原始参数进行转换，它的返回值就是路由函数参数接受的值
    def to_python(self, value):
        if value in self.true_values:
            return True
        else:
            return False


app.url_map.converters['bool'] = MyBoolConverter


@app.route('/my_converter/<bool:is_vip>')
def is_vip(is_vip):
    return f'is_vip: {is_vip}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)