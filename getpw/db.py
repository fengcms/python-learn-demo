#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sqlite3
import re

DB_PATH = 'passwd.db'

def checkDB(db):
    db.execute('''SELECT name FROM sqlite_master
		WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'
		ORDER BY 1''')
    o = db.fetchall()
    if len(o) == 0 or not bool(re.search(r'(\'passwd\',)',str(o))):
        db.execute('''CREATE TABLE passwd (
            id integer primary key autoincrement,
            name varchar(255),
            password varchar(255),
            time timestamp default current_timestamp
        )''')
def insertDb(name,passwd):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    c.execute("INSERT INTO passwd (name,password) VALUES ('" + name + "', '" + passwd + "')");
    conn.commit()

if __name__ == "__main__":
    insertDb('test','xxxx')
