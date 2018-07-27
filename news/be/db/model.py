#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.tool import rsaEncrypt
import config

DB_PATH = config.DB_CONN
KEY_PATH = config.PUBLIC_KEY_PATH

Base = declarative_base()
metadata = Base.metadata

engine = create_engine(DB_PATH)
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255, 0), nullable=False)
    channel_id = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    img = Column(String(255, 0))
    author = Column(String(255, 0))
    origin = Column(String(255, 0))
    editor = Column(String(255, 0))
    time = Column(TIMESTAMP, server_default=text("current_timestamp"))


class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    time = Column(TIMESTAMP, server_default=text("current_timestamp"))


class Manages(Base):
    __tablename__ = 'manages'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    time = Column(TIMESTAMP, server_default=text("current_timestamp"))


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    copyright = Column(Text)
    logo = Column(String(255))

# 根据模型创建数据库（如果数据库存在，则不会执行）
metadata.create_all(engine)

# 如果没有默认管理员，则添加上(默认密码123456)
if len(session.query(Manages).filter(Manages.id=='1').all()) == 0:
    defManage = Manages(username = 'admin', password = rsaEncrypt(KEY_PATH, '123456'))
    session.add(defManage)
    session.commit()

# 如果没有默认网站信息，则添加上
if len(session.query(Site).filter(Site.id=='1').all()) == 0:
    defSite = Site(name = '网站名称', title = '网站标题', copyright = '网站版权', logo = '')
    session.add(defSite)
    session.commit()
