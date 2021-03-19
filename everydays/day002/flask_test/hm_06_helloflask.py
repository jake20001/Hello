from flask import Flask, make_response, request,jsonify

app = Flask(__name__)


@app.route('/cookie')
def cookie():
    # 通过 request.cookies 读取当前客户端传递的 cookie
    print(request.cookies)
    return jsonify(request.cookies)


@app.route('/cookie/set')
def set_cookie():
    # 创建响应对象
    response = make_response('set cookies')

    # 设置响应头的set_cookie字段  value必须是str/bytes类型
    response.set_cookie('cookie-1', 'value-1', max_age=86400)
    response.set_cookie('cookie-2', 'value-2', max_age=86400)
    # 返回响应对象
    return response


@app.route('/cookie/delete')
def delete_cookie():
    # 创建响应对象
    response = make_response('delete cookies')
    # 通过 response.delete_cookie(cookie名) 删除 cookie
    response.delete_cookie('cookie-1')
    return response

@app.route('/cookie/delete/<one_cookie>')
def delete_cookie_one(one_cookie):
    # 创建响应对象
    response = make_response('delete cookies')
    # 通过 response.delete_cookie(cookie名) 删除 cookie
    response.delete_cookie(one_cookie)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)