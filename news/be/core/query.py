#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from db import model

session = model.DBSession()

def getDict(obj):
    d = {}
    for column in obj.__table__.columns:
        d[column.name] = getattr(obj, column.name)
    return d

def hasClass(className):
    try:
        getattr(model, className)
        return True
    except Exception as e:
        return False

def getFieldDict(Obj):
    res = {}
    for i in dir(Obj):
        if i[0] != '_' and i != 'id' and i != 'time':
            res[i] = ''
    return res

def ls(className, request):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        total = res.count()
        res = res.all()
        arr = []
        if res:
            for i in res:
                arr.append(getDict(i))
        return {'list': arr, 'total': total}
    except Exception as e:
        return 503

def post(className, Data):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        modelDict = getFieldDict(classModel)
        for i in Data:
            if i in modelDict:
                modelDict[i] = Data[i]
            else:
                return 400

        newData = classModel(**modelDict)
        session.add(newData)
        session.commit()
        return 200
    except Exception as e:
        return 503

def get(className, oid):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        if oid == 'first':
            res = res.first()
            if res == None:
                return 4043
            else:
                return getDict(res)
        else:
            res = res.filter_by(id=oid)
            try:
                res = res.one()
                return getDict(res)
            except Exception as e:
                return 4042

    except Exception as e:
        return 503

def put(className, oid, data):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        if oid == 'first':
            res = res.first()
            if res == None:
                return 4043
        else:
            res = res.get(oid)
            if res:
                oldData = getDict(res)
                for i in data:
                    if i not in oldData:
                        return 400
                    setattr(res, i, data[i])

                session.add(res)
                session.commit()
                return 200
            else:
                return 4042
    except Exception as e:
        return 503

def delete(className, oid):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel).get(oid)
        if res:
            session.delete(res)
            session.commit()
            return 200
        else:
            return 400
    except Exception as e:
        return 503
