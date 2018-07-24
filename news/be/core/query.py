#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from api import model

DB_PATH = 'sqlite:///' + sys.path[0] + '/news.db'
Base = declarative_base()
metadata = Base.metadata


engine = create_engine(DB_PATH)
DBSession = sessionmaker(bind=engine)
session = DBSession()
metadata.create_all(engine)

def getDict(obj):
    d = {}
    for column in obj.__table__.columns:
        d[column.name] = str(getattr(obj, column.name)) 
    return d

def hasClass(className):
    try:
        getattr(model, className)
        return True
    except Exception as e:
        return False

def ls(className):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        res = res.all()
        arr = []
        if res:
            for i in res:
                arr.append(getDict(i))
        return arr
    except Exception as e:
        return 500

def post(className, Data):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        newData = classModel(**Data)
        session.add(newData)
        session.commit()
        return 1 
    except Exception as e:
        return 500

def get(className, id):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        res = res.filter_by(id=id)
        res = res.one()
        return getDict(res)
    except Exception as e:
        return 500

def put(className, id, data):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel).get(id)
        if res:
            oldData = getDict(res)
            for i in data:
                if i not in oldData:
                    return 3
                setattr(res, i, data[i])

            session.add(res)
            session.commit()
            return 1
        else:
            return 2 
    except Exception as e:
        return 500

def delete(className, id):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel).get(id)
        if res:
            session.delete(res)
            session.commit()
            return 1
        else:
            return 2 
    except Exception as e:
        return 500
