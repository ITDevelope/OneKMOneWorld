import os

# 24位字符设置
SECRET_KEY = os.urandom(24)

# sql配置
# 在这里更改自己的数据库信息
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:19980425@localhost:3306/test1'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/testdb?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
