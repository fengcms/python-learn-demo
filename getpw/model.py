#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json


Base = declarative_base()
metadata = Base.metadata


class Passwd(Base):
    __tablename__ = 'passwd'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    time = Column(DateTime, server_default=text("current_timestamp"))

# 初始化数据库连接:
engine = create_engine('sqlite:///passwd.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = Passwd(name='Bob',password='love')
# 添加到session:
#session.add(new_user)
x = session.query(Passwd).get(2)
print(json.dumps({
    "name": x.name

    }))
#for i in session.query(Passwd).order_by(Passwd.id):
#    print(i.name)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
