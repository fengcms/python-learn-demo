#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from api import api
import config as c
from core.app import app

app.blueprint(api.bp)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = c.PORT)
