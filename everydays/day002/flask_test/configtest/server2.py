import os

from dotenv import load_dotenv
from flask import Flask, session



# 工厂函数: 根据参数需求, 内部封装对象的创建过程
from flask_test.configtest.config import config_dict

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# APP_DIR = os.path.dirname(BASE_DIR)
#
# load_dotenv(os.path.join(APP_DIR, 'secret_config.py'))

def create_app(config_type):
    """封装应用的创建过程"""

    # 创建应用
    flask_app = Flask(__name__)

    # 根据配置类型取出对应的配置子类
    config_class = config_dict[config_type]

    # 加载普通配置
    flask_app.config.from_object(config_class)

    return flask_app

# 创建应用对象
app = create_app('dev')

# 从环境变量中加载配置
# 优点: 可以保护隐私配置   export ENV_CONFIG="隐私配置的文件路径"

# SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
# prin`t(SECRET_KEY)

print(os.environ)

is_get = app.config.from_envvar('ENV_CONFIG1', silent=True)
print(is_get)

@app.route('/index')
def index():
    # 设置session 用于测试配置是否生效
    session['name'] = 'zs'
    # 读取配置
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    print(app.config.get('SECRET_KEY'))
    return "index"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)