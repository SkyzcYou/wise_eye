import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# from exts import db	#这里需要引入实例化的SQLAlchemy对象

"""
以下表关系：
一个用户对应多篇文章（一对多）
一篇文章对应多个标签，一个标签对应多个文章（多对多）
"""
"""
一对一关系中，需要设置relationship中的uselist=Flase，其他数据库操作一样。
一对多关系中，外键设置在多的一方中，关系（relationship）可设置在任意一方。
多对多关系中，需建立关系表，设置 secondary=关系表
"""

# 身份信息表
class AllInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(255))
    code = db.Column(db.String(255))
    indate = db.Column(db.DateTime,default=datetime.datetime.now)

# 增加：
# 现在时间：

info = AllInfo(image="image2123",code="522734198312270846")
db.session.add(info)
db.session.commit()