from flask import Flask, make_response,jsonify,redirect

app = Flask(__name__)

@app.route('/response_obj')
def response_obj():
    response = make_response('response content')
    response.headers['my-header'] = 'my-value'
    return response

@app.route('/response_json')
def response_json():
    data = {
        "name": "zhangsan",
        "age": 10
    }
    return "data"


# 老版本
@app.route('/response_jsonify')
def response_jsonify():
    data = {
        "name": "lisi",
        "age": 20
    }
    response = jsonify(data)
    return response


@app.route('/redirect')
def response_redirect():
    # redirect 中指定重定向的路径就可以
    return redirect('/response_jsonify')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
