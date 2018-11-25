import os
from datetime import datetime

from flask import (flash, get_flashed_messages, redirect, render_template,
                   request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

# 导入数据库
from app import app
from app import db
from .forms import upForm


# 主页


@app.route('/')
@app.route('/index')
def index():

    # 轮播区域
    post_bgs = [
        {
            'time': '2018-06-01',
            'author': 'Ming1',
            'title': 'titleA',
            'imag': '../static/images/home/01.jpg',  # 首页轮播图片为url,因此需要提前载入static
            'href_author': '#',  # 作者主页链接{{url_for()}}
            'href_blog': '#'  # 文章链接{{url_for()}}
        },
        {
            'time': '2018-06-02',
            'author': 'Ming2',
            'title': 'titleB',
            'imag': '../static/images/home/02.jpg',
            'href_author': '#',
            'href_blog': '#'
        }
    ]

    # 标准文章展示
    stand_as = [
        {
            'time': '2018-06-01',
            'author': 'Ming3',
            'title': '这里有非常好吃的东西',
            'like': '283',
            'view': '400',
            'comment': '20',
            'href_author': '#',
            'href_blog': '#',
            'imag': '../static/user_upload/images/01.jpg'
        },
        {
            'time': '2018-06-02',
            'author': 'Ming4',
            'title': '这里有非常好吃的东西+1',
            'like': '283',
            'view': '400',
            'comment': '20',
            'href_author': '#',
            'href_blog': '#',
            'imag': '../static/user_upload/images/02.jpg'
        }
    ]

    # 带音乐文章展示
    audio_as = [
        {
            'time': '2018-06-01',
            'author': 'Ming3',
            'title': '这里有非常好吃的东西',
            'like': '283',
            'view': '400',
            'comment': '20',
            'href_author': '#',
            'href_blog': '#',
            'imag': '../static/user_upload/images/03.jpeg',
            'audio':'../static/user_upload/audio/01.mp3'
        },
        {
            'time': '2018-06-01',
            'author': 'Ming3',
            'title': '这里有非常好吃的东西',
            'like': '283',
            'view': '400',
            'comment': '20',
            'href_author': '#',
            'href_blog': '#',
            'imag': '../static/user_upload/images/04.jpeg',
            'audio':'../static/user_upload/audio/02.mp3'
        }
    ]

    return render_template('index.html', post_bgs=post_bgs, stand_as = stand_as, audio_as=audio_as)


@app.route('/in', methods=['GET', 'POST'])
def upload():
    form = upForm()
    if request.method == 'POST' and form.validate():
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(
            basepath, 'static/images/user_upload', secure_filename(f.filename))
        f.save(upload_path)
        return '上传成功'
    return render_template('up.html', form=form, ds=ds)
