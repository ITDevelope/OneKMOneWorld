#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-05 12:24:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

# 导入数据库
# from app import app
# from app import db
# from .models import User, Client, Record, Share, Photo, Video

from math import radians, cos, sin, asin, sqrt

myLon=radians(113.3322640000)
myLat=radians(23.1562060000)

lon=radians(113.3280950000)
lat=radians(23.1653760000)

d = 2*asin(sqrt(pow(sin((myLat-lat)/2),2)+cos(lat)*cos(myLat)*pow(sin((myLon-lon)/2),2)))*6371*1000
print(d)