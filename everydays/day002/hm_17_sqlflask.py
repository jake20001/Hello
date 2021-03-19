# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/5 19:09
@Auth ： zhangjk
@File ：hm_17_sqlflask.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time

from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask,request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 创建组件对象
db = SQLAlchemy(app)

# 删除所有继承自db.Model的表
db.drop_all()

# 用户表  主表(一)   一个用户可以有多个地址
class User(db.Model):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    address = relationship('Address')  # 1.定义关系属性 relationship("关联数据所在的模型类")


# 地址表   从表(多)
class Address(db.Model):
    __tablename__ = 't_adr'
    id = Column(Integer, primary_key=True)
    detail = Column(String(20))
    # 2. 外键字段设置外键参数  ForeignKey('主表名.主键')
    user_id = Column(Integer, ForeignKey('t_user.id'))


@app.route('/relation/<user_name>')
def relation(user_name):
    def job(job_id,p1):
        print(job_id,p1,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


    # """添加并关联数据"""
    #     # user1 = User(name=user_name)
    #     # db.session.add(user1)
    #     # db.session.flush()  # 需要手动执行flush操作, 让主表生成主键, 否则外键关联失败
    #     # # db.session.commit()  # 有些场景下, 为了保证数据操作的原子性不能分成多个事务进行操作
    #     #
    #     # adr1 = Address(detail='中关村3号', user_id=user1.id)
    #     # adr2 = Address(detail='华强北5号', user_id=user1.id)
    #     # db.session.add_all([adr1, adr2])
    #     # db.session.commit()

    # 先根据姓名查找用户主键
    user1 = User.query.filter_by(name=user_name).first()

    # BlockingScheduler
    scheduler = BlockingScheduler()
    # scheduler.add_job(job, args=(user1,2),trigger="cron",day_of_week="1-5", hour=11, minute=58)
    scheduler.add_job(job, args=(user1,4),trigger="cron",day_of_week="1-5", hour=12, minute=2)
    scheduler .start()

    # 3.使用关系属性获取关系数据
    address = []
    add_dict = {}
    for adr in user1.address:
        address.append(adr.detail)
    add_dict[user_name] = address
    response = jsonify(add_dict)
    return response

@app.route('/join/<user_name>')
def join(user_name):
    """查询多表数据  需求: 查询姓名为"张三"的用户id和地址信息"""

    # sqlalchemy的join查询
    data = db.session.query(User.id, Address.detail).join(Address, User.id == Address.user_id).filter(User.name==user_name).all()
    address = {}
    for item in data:
        print(item.id, user_name, item.detail)
        address[item.id] = item.detail
    response = jsonify(address)

    return response


@app.route('/session')
def session():
    # 事务1
    try:
        name = request.args.get('name')
        address = request.args.get('address')
        user1 = User(name=name)
        db.session.add(user1)
        db.session.flush()
        # name 已经存在会报错
        adr1 = Address(detail=address, user_id=user1.id)
        db.session.add(adr1)
        db.session.commit()
        Result = 'OK'
    except BaseException:
        # 手动回滚 同一个session中, 前一个事务如果失败, 必须手动回滚, 否则无法创建新的事务
        db.session.rollback()
        Result = 'FAIL'

    return Result


if __name__ == '__main__':

    # 创建所有继承自db.Model的表
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)