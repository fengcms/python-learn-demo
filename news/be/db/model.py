#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

from core.tool import rsaEncrypt
import config
from config import DB_CONN, PUBLIC_KEY_PATH as KEY_PATH

Base = declarative_base()
metadata = Base.metadata

engine = create_engine(DB_CONN, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    edit_type = Column(String(255, 0), nullable=False)
    title = Column(String(255, 0), nullable=False)
    channel_id = Column(Integer, nullable=False)
    description = Column(Text)
    tags = Column(Text)
    content = Column(Text)
    markdown = Column(Text)
    img = Column(String(255, 0))
    author = Column(String(255, 0))
    origin = Column(String(255, 0))
    editor = Column(String(255, 0))
    time = Column(Integer, default=int(time.time()))

class Channel(Base):
    __tablename__ = 'channel'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer)
    name = Column(String(255), nullable=False)
    keywords = Column(Text)
    description = Column(Text)
    time = Column(Integer, default=int(time.time()))


class Manages(Base):
    __tablename__ = 'manage'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    time = Column(Integer, default=int(time.time()))

class Site(Base):
    __tablename__ = 'site'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    logo = Column(String(255))
    keywords = Column(Text)
    description = Column(Text)
    copyright = Column(Text)
    time = Column(Integer, default=int(time.time()))

class Author(Base):
    __tablename__ = 'author'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    mobile = Column(String(255))
    email = Column(String(255))
    website = Column(String(255))
    time = Column(Integer, default=int(time.time()))

class Origin(Base):
    __tablename__ = 'origin'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    contact = Column(String(255))
    mobile = Column(String(255))
    email = Column(String(255))
    website = Column(String(255))
    time = Column(Integer, default=int(time.time()))

class Editor(Base):
    __tablename__ = 'editor'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    name = Column(String(255), nullable=False)
    mobile = Column(String(255))
    email = Column(String(255))
    website = Column(String(255))
    time = Column(Integer, default=int(time.time()))

class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    tag = Column(String(255), nullable=False)
    channel_id = Column(Integer, nullable=False)
    hits = Column(Integer)
    time = Column(Integer, default=int(time.time()))


# 根据模型创建数据库（如果数据库存在，则不会执行）
metadata.create_all(engine)

# 如果没有默认管理员，则添加上(默认密码123456)
if len(session.query(Manages).all()) == 0:
    defManage = Manages(username = 'admin', password = rsaEncrypt(KEY_PATH, '123456'))
    session.add(defManage)
    session.commit()

# 如果没有默认网站信息，则添加上
if len(session.query(Site).all()) == 0:
    defSite = Site(name = '网站名称', title = '网站标题', copyright = '网站版权', logo = '')
    session.add(defSite)
    session.commit()
