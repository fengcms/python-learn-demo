#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
##########################################################################
# Name:    db.py                                                         #
# Author:  FungLeo                                                       #
# Date:    2017-12-20                                                    #
# Purpose: This program is used to generate simple or complex passwords  #
# Copy:    for study, prohibition of commercial use                      #
##########################################################################
import sqlite3
import re
import sys
from prettytable import PrettyTable
from pwlang import lang

DB_PATH = sys.path[0] + '/passwd.db'

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
    conn.close()

def selectDb(pid,name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)

    select = "SELECT * from passwd "
    if name:
        select += ('where name LIKE \'%' + name + '%\'')
    if pid:
        select += ('where id = \'' + str(pid) + '\'')
    select += 'ORDER BY id DESC'    

    res = list(c.execute(select))
    
    if len(res) == 0:
        print(lang('db_no_emp'))
    else:
        x = PrettyTable(['id','name','password','time'])
        x.align['name'] = 'l'
        x.padding_width = 1
        for row in res:
            x.add_row(list(row))
        print(x)
    conn.close()

def deleteDb(pid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    c.execute('DELETE from passwd where id=' + str(pid) )
    conn.commit()
    o = conn.total_changes
    if o == 0:
        print(lang('db_del_fail'))
    if o == 1:
        print(lang('db_del_succ_left') + str(pid) + lang('db_del_succ_right'))
    conn.close()
