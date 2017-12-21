#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'pw'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    time = Column(String(255))

# 初始化数据库连接:
engine = create_engine('sqlite:///passwd.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
