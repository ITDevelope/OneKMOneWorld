import os
import random
from datetime import datetime

from flask import flash, get_flashed_messages, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask import jsonify, Response
from math import radians, cos, sin, asin, sqrt

# 导入数据库
from app import app
from app import db
from .models import User, Client, Record, Share, Photo, Video
# 记得在config.py修改数据库配置,同时在终端使用db.create_all()命令创建表


@app.route('/map')
def showmap():

    # 验证session

    self_lon = 'self_lon'  # 获取经纬度,类型为浮点
    self_lat = 'self_lat'
    user_location = {
        'self_lon': self_lon,
        'self_lat': self_lat
    }
    all_shares = Share.query.all()
    select_shares = []  # 筛选符合距离的shares

    # 遍历式查询

    r = 6371.39  # 地球平均半径,精度10m(高德地图定位精度同为10m)

    for share in all_shares:
        share_lon = share.gps_lon  # 获取文章经纬度,float类型
        share_lat = share.gps_lat
        # Haversine算法计算距离
        lon1, lat1, lon2, lat2 = map(
            radians, [self_lon, self_lat, share_lon, share_lat])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        d = c * r * 1000
        if d <= 1:
            select_shares.append(share)

    # 查询完善信息
    shares = []
    for share in select_shares:
        if share.pid:
            post = {}
            post['img'] = Photo.query.filter_by(pid=share.pid).first().purl
            post['gps_lon'] = share.gps_lon
            post['gps_lat'] = share.gps_lat
            post['imgh'] = Photo.query.filter_by(
                pid=share.pid).first().psize_height
            post['imgw'] = Photo.query.filter_by(
                pid=share.pid).first().psize_width
            shares.append(post)

    return render_template('map.html', shares=shares, user_location=user_location)


@app.route('/maptest')
def maptest():

    user_location = {
        'self_lon': 116.4,
        'self_lat': 39.92
    }

    shares = [
        {
            'img': '1.jpg',
            'gps_lon': 116.35,
            'gps_lat': 39.89,
            'imgh': 70,
            'imgw': 105
        },
        {
            'img': '2.jpg',
            'gps_lon': 116.45,
            'gps_lat': 39.93,
            'imgh': 120,
            'imgw': 120
        }
    ]
    return render_template('map.html', shares=shares, user_location=user_location)
