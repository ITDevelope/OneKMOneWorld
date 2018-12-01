#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-11-13 09:08:58
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import Flask, request, render_template, redirect, url_for, session, jsonify

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/testdb?chrset=utf8'
#encoding:utf-8
#!/usr/bin/env python
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import time
from datetime import datetime
import base64
import cv2


# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF','wmv','asf','rm','rmvb','mov','avi','dat','mpg','mpeg'])
#  # 定义用户上传文件类型
#  # 
#  # 
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
 
# @app.route('/upload')
# def upload_test():
#     return render_template('upload.html')
 
 
# # 上传文件

# @app.route('/upload', methods=['POST', 'GET'])  # 添加路由
# def upload():
#     if request.method == 'POST':
#         f = request.files['file']
 
#         if not (f and allowed_file(f.filename)):
#             return jsonify({"error": 1001, "msg": "请检查上传的文件类型"})
 
#         user_input = request.form.get("tag")
#         message = request.form.get("message")
 
#         basepath = os.path.dirname(__file__)  # 当前文件所在路径
 
#         upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
#         f.save(upload_path)  #保存


#         # 使用Opencv转换一下图片格式和名称
#         img = cv2.imread(upload_path)
#         cv2.imwrite(os.path.join(basepath, 'static/images', 'test.jpg'), img)
 
#         return render_template('upload_ok.html',userinput=user_input,Message = message,msg="发表成功")
#  			# 用户输入的标签为userinput
#     return render_template('upload.html')




 
if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=8987, debug=True) #测试图文端口设置

@news_blu.route("/<int:news_id>")
@user_login_data
@click_list_data
def news_detail(news_id):
    # 显示新闻
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        abort(404)
    if not news:
        abort(404)
    news.clicks +=1

    # 是否收藏
    iscollected = False
    if g.user:
        if news in g.user.collection_news:
            iscollected = True

    # 显示评论
    try:
        comments = Comment.query.filter(Comment.news_id == news_id).order_by(Comment.create_time.desc()).all()
    except Exception as e:
        current_app.logger.error(e)
        comments = []

    # 点赞功能显示------------------------------
    # 找出用户所有点赞的评论的ｉｄ
if g.user:
        comment_like_ids = [commentlike.comment_id for commentlike in CommentLike.query.filter(CommentLike.user_id == g.user.id).all()]
    else:
        comment_like_ids = []
    # 如果评论在用户点赞的评论中，那么显示点赞
    comment_list = []
    for comment in comments:
        com = comment.to_dict()
        com["is_like"] = False
        if g.user and comment.id in comment_like_ids:
            com["is_like"] = True
        comment_list.append(com)

    # 按接口返回数据
    data = {"news":news.to_dict(),
            "user_info":g.user.to_dict() if g.user else None,
            "clicks_list":g.clicks,
            "is_collected": iscollected,
            "comments": comment_list
            }
    return render_template("/news/detail.html", data=data)
