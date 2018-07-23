#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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


class Manage(Base):
    __tablename__ = 'manages'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    time = Column(TIMESTAMP, server_default=text("current_timestamp"))


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    copyright = Column(Text)
    logo = Column(String(255))
