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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test?charset=utf8'
db.create_all()
@app.route('/index') #主页
def index():
    return render_template('index.html')

# 登陆
@app.route('/login')
def login():
    return render_template('login.html')



# 个人主页
@app.route('/user/<useruid>', methods=['GET', 'POST'])
def author(useruid):
    # 验证session
    uid=session['uid']='1'
    # try:
    #     uid = session['uid']
    # except:
    #     flash('请先登陆')
    #     return render_template('login.html', flash=flash)

    user = {
    'username': '1',
    'email':'888@qq.com',
    'sign':'666666',
    'like_count':'888',
    'score':'100',
    'img' : "images/1.jpg"
      } 
    shares = [{
    'text':'此次出行很开心 喜欢这种古镇的感觉 ',
    'img' : "images/2.jpg",
    'tag':'风景'
       },
       {
    'text':'期待这个地方很久了……果然很棒， 在苍茫的北方大地上还有这样一处幽地，像是到了江南水乡，温婉多姿。夜景也很给力，终于可以远离喧闹，安安静静的休息一下了…………特别开心可以和心爱的人来这玩………',
    'collected_count':'90',
    'img' : 'images/3.jpg',
    'tag':'风景'
       }]

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        sign = request.form.get('sign')
        icon = request.files['icon']
        # 上传用户头像
        basepath = os.path.dirname(__file__)
        upload_path_icon = os.path.join(
            basepath, 'static/upload', secure_filename(icon.filename))  # 文件存入服务器
        icon.save(upload_path_icon)
        upload_path_icon = os.path.join(
            'upload/icon', secure_filename(icon.filename))

        User.query.filter_by(uid=session['uid']).update({  # 更新
            'username': username,
            'email': email,
            'icon': upload_path_icon
        })
        Client.query.filter_by(uid=session['uid']).update({ #更新
        	'sign': sign
        	})
                    


        db.session.commit()
    return render_template('author-info.html',user=user,shares=shares,uid=uid)

@app.route('/xxx/<share_id>')
def view(share_id):
	return '0'

