from six import PY3
from json import dumps
from flask import Flask, current_app, make_response
from flask_restful import Resource, Api
from werkzeug.http import HTTP_STATUS_CODES

app = Flask(__name__)
api = Api(app)

# 自定义输出 json 的格式
@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262

    # 添加消息，如果 data 中有 message 就取出 message，如果没有就用 HTTP 中 code 对应的 message
    message = data.pop('message', None)
    # 如果没有 message 就用 HTTP 中 code 对应的 message
    if not message:
        # from werkzeug.http import HTTP_STATUS_CODES
        message = HTTP_STATUS_CODES.get(code, '')
    data = {
        'code': code,
        'message': message,
        'data': data
    }

    dumped = dumps(data, **settings) + "\n"

    # resp = make_response(dumped, code)
    # 这里统一返回 200 响应，客户端通过判断响应体的 code 字段
    resp = make_response(dumped, 200)
    resp.headers.extend(headers or {})
    return resp


class DemoResource(Resource):
    def get(self):
        return {'get': 'foo'}


api.add_resource(DemoResource, '/response')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)