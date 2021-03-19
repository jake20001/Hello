from flask import Flask

app = Flask(__name__)


# 定义路由变量
@app.route('/user/<user_id>')
def index(user_id):
    return f"user_id: {user_id}"
# app.add_url_rule('/user/<user_id>',None, index)

# # string
# @app.route('/string/<string(minlength=1,maxlength=16):username>')
# def username(username):
#     return f'username: {username}'
#
#
# # any
# @app.route('/any/<any("home","cart","order"):page_name>')
# def page_name(page_name):
#     return f'page_name: {page_name}'
#
#
# # path
# @app.route('/path/<path:file_path>')
# def file_path(file_path):
#     return f'file_path: {file_path}'
#
#
# # int
# @app.route('/int/<int(min=10,max=100):age>')
# def age(age):
#     return f'age: {age}'
#
#
# # float
# @app.route('/float/<float(min=0,max=10):score>')
# def score(score):
#     return f'score: {score}'
#
#
# # uuid
# @app.route('/uuid/<uuid:image_code_id>')
# def image_code_id(image_code_id):
#     return f'image_code_id: {image_code_id}'


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)