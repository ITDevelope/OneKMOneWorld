#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-11-13 09:07:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from app.router import app

app.secret_key = os.urandom(24)
app.run(host='0.0.0.0', port = 8000, debug = True)