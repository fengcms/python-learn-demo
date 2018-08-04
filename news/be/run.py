#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from api import be
from api import fe
import config as c
from core.app import app

print(fe.bpfe)

app.blueprint(fe.bpfe)
app.blueprint(be.bp)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = c.PORT)
