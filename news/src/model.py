#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

DB_PATH = 'sqlite:///' + sys.path[0] + '/news.db'

Base = declarative_base()
metadata = Base.metadata


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    channel_id = Column(Integer)
    author = Column(String(255))
    origin = Column(String(255))
    content = Column(Text)
    img = Column(String(255))
    time = Column(DateTime, server_default=text("current_timestamp"))

engine = create_engine(DB_PATH)
DBSession = sessionmaker(bind=engine)
session = DBSession()
metadata.create_all(engine)

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def insertDb(dat):
    new_art = Article(
        title = dat.get('title'),
        channel_id = dat.get('channel_id'),
        author = dat.get('author') or '',
        origin = dat.get('origin') or '',
        content = dat.get('content'),
        img = dat.get('img') or '',
    )
    session.add(new_art)
    session.commit()

def readDb(args):
    pagesize = args.get('pagesize') or 10
    page = args.get('page') or 0
    res = []
    dat = session.query(Article).offset(page).limit(pagesize)
    for i in dat:
        res.append(row2dict(i))
    return res
