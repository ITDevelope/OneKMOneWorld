#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-11-13 09:21:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
from flask_sqlalchemy import SQLAlchemy

sys.path.append("..")
from router import app

# db = SQLAlchemy(app)