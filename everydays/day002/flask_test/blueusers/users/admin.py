#1创建一个蓝图对象
from flask import Blueprint

index_blue = Blueprint("Test",__name__)


#2注册路由
@index_blue.route('/edit')
def edit():
    return 'edit'