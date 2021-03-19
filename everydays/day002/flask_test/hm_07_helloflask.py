from datetime import timedelta
from flask import Flask, session,jsonify

app = Flask(__name__)
# 设置应用秘钥会被用于session签名
app.secret_key = 'test'
# 设置session过期时间 默认31天
print(f'默认过期时间: {app.permanent_session_lifetime}')
# 通过赋值一个 timedelta 对象来修改 session 的过期时间
app.permanent_session_lifetime = timedelta(days=0,seconds=20)
print(f'测试过期时间: {app.permanent_session_lifetime}')


@app.route('/session')
def get_session():
    # session是一个类字典对象
    print(session)
    return jsonify({key: value for key, value in session.items()})


@app.route('/session/set')
def set_session():
    # session是一个类字典对象, 对其取值/赋值 就可以实现session数据的读写

    # 记录session数据
    session['username'] = 'zhangsan'
    session['age'] = 100

    return "set session"


@app.route('/session/delete')
def delete_session():
    # 使用 del 来删除 session 的 key，但是要判断 key 是否在 session，如果不判断可能会出现异常
    if 'username' in session:
        del session['username']
    return "delete session"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)