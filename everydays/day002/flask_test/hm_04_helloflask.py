import os

from flask import Flask

app = Flask(__name__,
            static_folder="static",  # 设置静态文件的存储目录
            static_url_path='/static',  # 设置静态文件的URL访问路径 如 127.0.0.1:5000/static/test.png
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
