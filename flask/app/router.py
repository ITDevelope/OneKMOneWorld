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


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF','wmv','asf','rm','rmvb','mov','avi','dat','mpg','mpeg'])
 # 定义用户上传文件类型
 # 
 # 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
 
@app.route('/upload')
def upload_test():
    return render_template('upload.html')
 
 
# 上传文件

@app.route('/upload', methods=['POST', 'GET'])  # 添加路由
def upload():
    if request.method == 'POST':
        f = request.files['file']
 
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的文件类型"})
 
        user_input = request.form.get("tag")
        message = request.form.get("message")
 
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
 
        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)  #保存


        # 使用Opencv转换一下图片格式和名称
        img = cv2.imread(upload_path)
        cv2.imwrite(os.path.join(basepath, 'static/images', 'test.jpg'), img)
 
        return render_template('upload_ok.html',userinput=user_input,Message = message,msg="发表成功")
 			# 用户输入的标签为userinput
    return render_template('upload.html')




 
if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=8987, debug=True) #测试图文端口设置
