import os
import random
from datetime import datetime

from flask import flash, get_flashed_messages, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask import jsonify, Response

# 导入数据库
from app import app
from app import db
from .models import User, Client, Record, Share, Photo, Video
# 记得在config.py修改数据库配置,同时在终端使用db.create_all()命令创建表
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/testdb?charset=utf8'

@app.route('/index') #主页
def index():
    return render_template('index.html')

@app.route('/author/<authoruid>', methods=['GET', 'POST']) 
def authorinfo():
	return render_template('author-info.html')