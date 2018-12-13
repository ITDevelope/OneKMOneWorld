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

db.create_all()

# 图文模式主页面————session（id，用户名，头像，等级？，总积分，位置），一公里内的发布的数据（默认按时间排序）（图片/视频缩略图，描述，标签，发布时间，浏览次数，评论数，点赞数），
@app.route('/index', methods=['GET'])
def index():
	
	session['uid'] = 1
	session['username'] = 1

	try:
		uid = session['uid']
		username = session['username']
	except:
		flash('请先登录')
		# return render_template('login.html', flash=flash)
		return render_template(flash=flash)

	#每次刷新页面，从前端获取当前位置
	myLon = request.args['lon']
	myLat = request.args['lat']
	time = datetime.now()

	# 一公里内的文章，按时间排序
	distance = '(2*asin(sqrt(pow(sin((radians(:myLat)-radians(lat))/2),2)+cos(radians(lat))*cos(radians(:myLat))*pow(sin((radians(:myLon)-radians(lon))/2),2)))*6371*1000)'
	sql = " select s.uid, s.share_id, s.text, s.tag, s.share_time, s.view_count, s.comment_count, s.like_count, s.collected_count, u.username, u.uid, (case when s.pid is null then 'v' else 'p' end) as type, p.purl, v.vurl, " + distance +" as distance from share as s inner join clients as u on s.uid=u.uid left join photos as p on s.pid=p.pid left join videos as v on s.vid=v.vid where " + distance + " < 1000 order by share_time desc"

	# 标准文章展示
	# uid, share_id, text, tag, share_time, view_count, comment_count, like_count, collected_count, username, type, purl, vurl
	blogs = db.session.execute(sql,{"myLat":myLat,"myLon":myLon}).fetchall()
	ilikes = []
	for blog in blogs:
		r = Record.query.filter_by(share_id=blog.share_id, uid=session['uid'], like=1).all()
		if len(r)>0:
			ilikes.append(Record.query.filter_by(share_id=blog.share_id, uid=session['uid'], like=1).order_by('-time').first().like)
		else:
			ilikes.append(0)

	# 轮播区域
	post_bgs = []
	if(len(blogs)>0):
		# 轮播区域
		for i in range(1):
			post_bg = {}
			post_bg['time'] = blogs[i].share_time
			post_bg['author'] = Client.query.filter_by(uid=blogs[i].uid).first().username
			if blogs[i].type == 'p':
				post_bg['img'] = blogs[i].purl
			else:
				post_bg['img'] = blogs[i].vurl
			post_bg['authorid'] = blogs[i].uid
			post_bg['blogid'] = blogs[i].share_id
			post_bgs.append(post_bg)
   
	    
	return render_template('index.html', username=username, post_bgs=post_bgs, blogs=blogs, ilikes=ilikes)

# 点赞及取消点赞
@app.route('/like/<bid>')
def like(bid):
	record = Record.query.filter_by(uid=session['uid'], share_id=bid).order_by('-time').first()
	time = datetime.now()
	if record is None or record.like==0:
		r = Record(uid=session['uid'], comment='', like=1, collect=0, share_id=bid, time=time)
		db.session.add(r)
		db.session.commit()
		msg = '点赞成功'
	else:
		r = Record(uid=session['uid'], comment='', like=0, collect=0, share_id=bid, time=time)
		db.session.add(r)
		db.session.commit()
		msg = '取消点赞'
	return msg

@app.route('/comment/<bid>', methods=['POST'])
def comment(bid):
	comment = request.form.get('comment')

	time = datetime.now()

	r = Record(uid=session['uid'], comment=comment, like=0, collect=0, share_id=bid, time=time)
	db.session.add(r)
	db.session.commit()
	msg = '评论成功'

	return redirect(url_for('blog',bid=bid))

@app.route('/collect/<bid>')
def collect(bid):
	record = Record.query.filter_by(uid=session['uid'], share_id=bid).order_by('-time').first()
	time = datetime.now()
	if record is None or record.collect==0:
		r = Record(uid=session['uid'], comment='', like=0, collect=1, share_id=bid, time=time)
		db.session.add(r)
		db.session.commit()
		msg = '收藏成功'
	else:
		r = Record(uid=session['uid'], comment='', like=0, collect=0, share_id=bid, time=time)
		db.session.add(r)
		db.session.commit()
		msg = '取消收藏'
	return msg

@app.route('/profile/<uid>')
def profile(uid):
	pass

@app.route('/blog/<bid>')
def blog(bid):
	time = datetime.now()
	new_record = Record(uid=session['uid'], comment='', like=0, collect=0, share_id=bid, time=time)
	try:
		blog = Share.query.filter_by(share_id=bid).first()
	except:
		return "内容不存在！"

	author_info = db.session.query(User.uid, User.username, User.icon, User.sign).filter(User.uid==blog.uid).first()
	comments = db.session.query(Record.comment, Record.time, Record.uid, User.username, User.icon).join(User, Record.uid==User.uid).filter(Record.share_id==bid).all()
	if blog.pid:
		purl = Photo.query.filter_by(pid=blog.pid).first().purl
		return render_template('single-standard.html', style='format-standard', blog=blog, purl=purl, author_info=author_info, comments=comments)
	else:
		vurl = Video.query.filter_by(vid=blog.vid).first().vurl
		return render_template('single-video.html', style='format-audio', blog=blog, vurl=vurl, author_info=author_info, comments=comments)