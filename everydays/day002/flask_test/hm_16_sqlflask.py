# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/5 11:29
@Auth ： zhangjk
@File ：hm_16_sqlflask.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from flask import Flask,request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

# 应用配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 方式1: 初始化组件对象, 直接关联Flask应用
db = SQLAlchemy(app)

# 删除所有继承自db.Model的表
db.drop_all()


# 构建模型类  类->表  类属性->字段  实例对象->记录
class User(db.Model):
    __tablename__ = 't_user'  # 设置表名, 表名默认为类名小写
    id = Column(Integer, primary_key=True)  # 设置主键, 默认自增
    name = Column('username', String(20), unique=True)  # 设置字段名 和 唯一约束
    age = Column(Integer, default=10, index=True)  # 设置默认值约束 和 索引


# 地址表   从表(多)
class Address(db.Model):
    __tablename__ = 't_adr'
    id = Column(Integer, primary_key=True)
    detail = Column(String(20))
    user_id = Column(Integer)  # 定义外键


@app.route('/add')
def index():
    """增加数据"""
    reqs = request.args
    name = reqs.get("name")
    age = reqs.get("age")
    # 1.创建模型对象
    user1 = User(name=name, age=age)
    # 2.将模型对象添加到会话中
    db.session.add(user1)
    # 添加多条记录
    # user2 = User(name='lisi',age=10)
    # user3 = User(name='ww',age=15)
    # db.session.add_all([user2, user3])

    # 3.提交会话 (会提交事务)
    # sqlalchemy 会自动创建隐式事务
    # 主动执行flush操作, 立即执行SQL操作(数据库同步)
    db.session.flush()
    # 事务失败会自动回滚
    db.session.commit()

    return "index"


@app.route('/find')
def find():
    # use_dict = {}
    # ax = []
    dxt = {}
    # 查询所有用户数据,返回列表, 元素为模型对象
    users = User.query.all()
    for user in users:
        name = user.name
        age = user.age
        dxt[name] = age
        # ax.append(dxt)
    # use_dict['app'] = ax
    response = jsonify(dxt)
    return response

@app.route('/select_then_update/<user_name>')
def select_then_update(user_name):
    """先查询, 再更新"""

    # 更新方式1: 先查询后更新
    # 缺点: 并发情况下, 容易出现更新丢失问题 (Lost Update)

    # # 1.执行查询语句, 获取目标模型对象 : 方式 1
    # user = User.query.filter(User.name==user_name).first()
    # # 2.对模型对象的属性进行赋值 (更新数据)
    # user.age = user.age+50
    # 方式 2
    User.query.filter(User.name == user_name).update({'age': User.age - 1})
    # 主动执行flush操作, 立即执行SQL操作(数据库同步)
    db.session.flush()
    # 3.提交会话
    db.session.commit()

    return "select_then_update"


@app.route('/add_relation')
def add_relation():
    """添加并关联数据"""
    user1 = User(name='张三',age=27)
    db.session.add(user1)
    db.session.flush()  # 需要手动执行flush操作, 让主表生成主键, 否则外键关联失败
    # db.session.commit()  # 有些场景下, 为了保证数据操作的原子性不能分成多个事务进行操作

    adr1 = Address(detail='中关村3号', user_id=user1.id)
    adr2 = Address(detail='华强北5号', user_id=user1.id)
    db.session.add_all([adr1, adr2])
    db.session.flush()
    db.session.commit()

    return "add_relation"


@app.route('/query_relation/<user_name>')
def query_relation(user_name):
    """查询多表数据  需求: 查询姓名为"张三"的所有地址信息"""

    # 1.先根据姓名查找到主表主键
    user1 = User.query.filter_by(name=user_name).first()

    # 2.再根据主键到从表查询关联地址
    adrs = Address.query.filter_by(user_id=user1.id).all()
    address = []
    add_dict = {}
    for adr in adrs:
        address.append(adr.detail)
    add_dict[user_name] = address
    response = jsonify(add_dict)
    return response


@app.route('/select_then_delete/<user_name>')
def select_then_delete(user_name):
    """先查询, 再删除"""

    # # 方式1: 先查后删除
    # user = User.query.filter(User.name==user_name).first()
    # # 删除数据
    # db.session.delete(user)
    # 方式2: delete子查询
    User.query.filter(User.name==user_name).delete()
    # 主动执行flush操作, 立即执行SQL操作(数据库同步)
    db.session.flush()
    # 提交会话 增删改都要提交会话
    db.session.commit()

    return "select_then_delete"


if __name__ == '__main__':
    # 创建所有继承自db.Model的表
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)