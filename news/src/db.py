#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sqlite3
import re
import os
import sys

DB_PATH = sys.path[0] + '/news.db'
INIT_DB_SQL = sys.path[0] + '/__init_db.sql'

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

def checkDb(db):
    db.execute('''SELECT name FROM sqlite_master
                WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'
                ORDER BY 1''')
    o = db.fetchall()
    if len(o) == 0:
        if os.path.exists(INIT_DB_SQL):
            init_file = open(INIT_DB_SQL)
            init_sql = init_file.read()
            db.execute(init_sql)
            init_file.close()
            checkDb(db)
        else:
            print(INIT_DB_SQL + ' is not find')

def insertDb(sql):
    c.execute(sql)
    conn.commit()
#---
checkDb(c)
