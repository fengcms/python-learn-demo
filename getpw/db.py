#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from prettytable import PrettyTable

DB_PATH = 'sqlite:///' + sys.path[0] + '/passwd.db'
Base = declarative_base()
metadata = Base.metadata


class Passwd(Base):
    __tablename__ = 'passwd'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    time = Column(DateTime, server_default=text("current_timestamp"))

engine = create_engine(DB_PATH)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def obj2list(obj):
    d = []
    for column in obj.__table__.columns:
        d.append(str(getattr(obj, column.name)))
    return d
def insertDb(n, pw):
    new_pw = Passwd(name=n,password=pw)
    session.add(new_pw)
    session.commit()

def selectDb(pid, name):
    res = session.query(Passwd)

    x = PrettyTable(['id','name','password','time'])
    x.align['name'] = 'l'
    x.padding_width = 1
    
    if pid:
        res = res.filter_by(id = pid)
    elif name:
        res = res.filter(Passwd.name.like('%' + name + '%'))
    res = res.all()
    if not res:
        print('Info: record is empty')
        exit()

    for i in res:
        x.add_row( obj2list(i) )

    print(x)
def deleteDb(pid):
    de = session.query(Passwd).get(pid)
    if de:
        session.delete(de)
        session.commit()
        print('Success: ID ' + str(pid) + ' password has been deleted')
    else:
        print('Failure: the password was not found')

