# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/3/13 15:29
# FileName : context_processor_钩子
# Description : 
# --------------------------------

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def list():
    return render_template('list.html')


@app.context_processor
def context_processor():
    return {'current_user':'aaa'}


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)