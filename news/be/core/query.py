#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sqlalchemy import desc
from db import model
import config

PS = config.PAGESIZE

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

def getFieldList(Obj):
    res = []
    for i in dir(Obj):
        if i[0] != '_':
            res.append(i)
    return res

def ls(className, request):
    if not hasClass(className):
        return 404
    try:
        # 从请求参数中获取非标准参数
        arcs = {}
        for i in request:
            i = i.lower()
            if not i in ['page', 'pagesize', 'sort']:
                arcs[i] = request[i]

        # 请求全量数据，并统计总条数
        classModel = getattr(model, className)
        modelList = getFieldList(classModel)
        res = session.query(classModel).filter_by(**arcs)
        total = res.count()


        # 获取排序参数
        sort = 'id' if not 'sort' in request else request['sort']
        # 支持多重条件排序，用英文逗号分隔
        sortArr = sort.split(',')
        for i in sortArr:
            ## 根据排序参数第一个字符是否是中划线确定是正序还是倒序，为假倒序
            sortType = i[0] == '-'
            sortField = i[1:] if sortType else i
            if not sortField in modelList:
                return 400
            if sortType:
                res = res.order_by(getattr(classModel, sortField))
            else:
                res = res.order_by(getattr(classModel, sortField).desc())

        # 获取分页序号参数
        page = 0 if not 'page' in request else request['page']
        if not page.isdigit():
            return 400
        else:
            page = int(page)

        # 获取分页每页数量参数
        pagesize = PS if not 'pagesize' in request else request['pagesize']
        if not pagesize.isdigit():
            return 400
        else:
            pagesize = int(pagesize)

        res = res.limit(pagesize).offset(page * pagesize)
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
