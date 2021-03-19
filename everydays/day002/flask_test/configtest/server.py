from flask import Flask, session

from flask_test.configtest.config import Development,Production

app = Flask(__name__)

# 加载配置
app.config.from_object(Production)


@app.route('/index')
def index():
    # 设置session 用于测试配置是否生效
    session['name'] = 'zs'
    # 读取配置
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    return "index"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
