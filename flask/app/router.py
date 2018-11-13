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