from flask import Flask, request

app = Flask(__name__)


# 请求的基础数据
@app.route('/base_info', methods=['get', 'post'])
def base_info():
    print(f'url: {request.url}')  # 请求的URL
    print(f'method: {request.method}')  # 本次请求的请求方式
    print(f'headers: {request.headers}')  # 获取请求头信息  类字典对象

    print(f'header-host: {request.headers["Host"]}')
    print(f'header-host: {request.headers.get("Host")}')  # 建议使用get方法, 键不存在不报错

    return 'base_info'

# 获取查询字符串、表单
@app.route('/args_form', methods=['get', 'post'])
def args_form():
    # 获取查询字符串 -> request.args  xx?name=zs&age=20  类字典对象
    print(request.args)
    print(request.args.get('a'))
    print(request.args.get('b'))
    # 获取参数所有值
    print(request.args.getlist('b'))

    # 获取post键值对 -> request.form  类字典对象
    print(request.form)
    print(request.form.get('form-a'))
    # 获取参数所有值
    print(request.form.getlist('form-a'))

    return 'args_form'

# 获取请求体数据原始字节数据、json 请求字典
@app.route('/data_json', methods=['get', 'post'])
def data_json():
    # request.data 获取请求体数据原始字节数据
    print(request.data)  # 返回bytes类型
    # request.json 直接将 json 请求体转为字典
    print(request.json)
    return 'data_json'

# 上传的文件
@app.route('/files', methods=['get', 'post'])
def files():
    #  request.files 获取用户上传的文件，类字典对象
    print(request.files)
    file1 = request.files.get("upload_file_1")  # type: FileStorage
    print(type(file1))  # 返回 FileStorage文件对象
    # 将文件保存到本地
    file1.save('test.png')

    # 获取文件的二进制数据
    file2 = request.files.get("upload_file_2")
    img_bytes = file2.read()
    print(img_bytes)

    return "files"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)