#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-03 09:03:03
# @Author  : hyy (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

from math import radians, cos, sin, asin, sqrt

def getDistance(lon1, lat1, lon2, lat2):
	"""
	Calculate the great circle distance between two points
	By longitude and latitude

	"""

	# 将十进制度数转化为弧度
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	# Harversine 半正矢公式
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	distance = 2*asin(sqrt(a))*6371*1000

	return distance

print(getDistance(116.368904, 39.923423, 116.387271, 39.922501))
