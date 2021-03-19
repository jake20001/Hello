# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/7 11:45
@Auth ： zhangjk
@File ：hm_18_sqlflask.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from flask import Flask,request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from flask_migrate import Migrate

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 创建组件对象
db = SQLAlchemy(app)

# 迁移组件初始化
Migrate(app, db)


# 构建模型类
class User(db.Model):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True)
    name = Column("name",String(20), unique=True)
    age = Column(Integer, default=0, index=True)
    address = Column(String(128))
    dad = Column(String(128))

@app.route('/add')
def add_user():
    """增加数据"""
    reqs = request.args
    name = reqs.get("name")
    age = reqs.get("age")
    address = reqs.get("address")
    dad = reqs.get("dad")
    # 1.创建模型对象
    user1 = User(name=name, age=age,address=address,dad=dad)
    # 2.将模型对象添加到会话中
    db.session.add(user1)
    # 主动执行flush操作, 立即执行SQL操作(数据库同步)
    db.session.flush()
    # 事务失败会自动回滚
    db.session.commit()
    return jsonify({'name':name,'age':age})


@app.route('/add_father/<user_name>/<id>')
def add_father(user_name,id):
    dad = request.args.get("dad")
    user = User.query.filter_by(name=user_name, id=id).first()
    user.dad=dad
    db.session.commit()
    return 'OK'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)