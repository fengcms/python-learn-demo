#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import isInt
from db import model
from config import PAGESIZE
from sqlalchemy import text
import time

session = model.DBSession()

# 将数据库查询数据变成字典型方法
def getDict(obj):
    d = {}
    for column in obj.__table__.columns:
        d[column.name] = getattr(obj, column.name)
    return d

# 根据字符串判断数据库是否包含该表
def hasClass(className):
    try:
        getattr(model, className)
        return True
    except Exception as e:
        return False

# 传入模型，获得该模型字段字典并赋空值，排除id和time，用于post方法
def getFieldDict(Obj):
    res = {}
    for i in dir(Obj):
        if i[0] != '_' and i != 'id' and i != 'time':
            res[i] = ''
    return res

# 传入模型，获得该模型字段列表, 用于 ls 方法
def getFieldList(Obj):
    res = []
    for i in dir(Obj):
        if i[0] != '_':
            res.append(i)
    return res

# 查询列表方法
def ls(className, request):
    if not hasClass(className):
        return 404
    try:
        # 从请求参数中获取非标准参数
        args = {}
        for i in request:
            i = i.lower()
            if not i in ['page', 'pagesize', 'sort', 'time']:
                args[i] = request[i]

        # 获得模型，以及支持的字段数组列表
        classModel = getattr(model, className)
        modelList = getFieldList(classModel)

        # 开始查询数据
        res = session.query(classModel)
        
        # 处理时间特性
        if 'time' in request:
            tArr = request['time'].split('-')
            if len(tArr) > 2:
                return 400
            for i in tArr:
                if not isInt(i):
                    return 400
            if len(tArr) == 1:
                t = int(tArr[0])
                st = t - (t + 28800)%86400
                et = st + 86400
            else:
                st = int(tArr[0])
                et = int(tArr[1])
            field = getattr(classModel, 'time')
            res = res.filter(field < et).filter(field >= st)

        # 处理各种非标准参数查询
        for i in args:
            # 支持一个条件带多个参数，用英文逗号分割
            argVal = args[i].split(',')
            arg = i.split('-')
            argField = arg[0]
            argMethod = None if len(arg) == 1 else arg[1]
            field = getattr(classModel, argField)
            # 检查字段是否是模型支持的
            if not argField in modelList:
                return 400
            # 处理特殊查询条件
            if argMethod:
                # 模糊查询
                if argMethod == 'like':
                    for val in argVal:
                        res = res.filter(field.like('%' + val + '%'))
                # 不等于查询
                elif argMethod == 'neq':
                    for val in argVal:
                        res = res.filter(field != val)
                # 大于查询
                elif argMethod == 'gt' and len(argVal) == 1:
                    res = res.filter(field > argVal[0])
                # 大于等于查询
                elif argMethod == 'gteq' and len(argVal) == 1:
                    res = res.filter(field >= argVal[0])
                # 小于查询
                elif argMethod == 'lt' and len(argVal) == 1:
                    res = res.filter(field < argVal[0])
                # 小于等于查询
                elif argMethod == 'lteq' and len(argVal) == 1:
                    res = res.filter(field <= argVal[0])
                # in List 查询
                elif argMethod == 'in':
                    res = res.filter(field.in_(argVal))
                # not in List 查询
                elif argMethod == 'nin':
                    res = res.filter(~field.in_(argVal))
                # 其他不支持关键词返回参数错误
                else:
                    return 400
            # 处理普通相等查询条件
            else:
                for val in argVal:
                    res = res.filter(field == val)

        # 获取排序参数
        sort = 'id' if not 'sort' in request else request['sort']

        # 支持多重条件排序，用英文逗号分隔
        sortArr = sort.split(',')
        for i in sortArr:
            # 根据排序参数第一个字符是否是中划线确定是正序还是倒序，为假倒序
            sortType = i[0] == '-'
            sortField = i[1:] if sortType else i

            field = getattr(classModel, sortField)

            if not sortField in modelList:
                return 400
            if sortType:
                res = res.order_by(field)
            else:
                res = res.order_by(field.desc())

        # 统计总条数
        total = res.count()

        # 获取分页序号参数
        page = 0 if not 'page' in request else request['page']
        if not isInt(page):
            return 400
        else:
            page = int(page)

        # 获取分页每页数量参数
        pagesize = PAGESIZE if not 'pagesize' in request else request['pagesize']
        if not isInt(pagesize):
            return 400
        else:
            pagesize = int(pagesize)

        # 处理分页和分页需要查询 如果 pagesize 为 -1 则全部输出
        if pagesize == -1:
            res = res.all()
        else:
            res = res.limit(pagesize).offset(page * pagesize)

        # 将结果整理成列表输出
        arr = []
        if res:
            for i in res:
                arr.append(getDict(i))
        return {'list': arr, 'total': total}

    except Exception as e:
        print(e)
        return 503

# 添加新数据方法
def post(className, request):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        modelDict = getFieldDict(classModel)
        resIds = []
        for Data in request['data']:
            for i in Data:
                if i in modelDict:
                    modelDict[i] = Data[i]
                else:
                    return 400
            newData = classModel(**modelDict)
            session.add(newData)
            session.flush()
            session.commit()
            resIds.append(newData.id)
        # 将自增ID返回
        return {'id': resIds}
    except Exception as e:
        return 503

# 查询单条数据方法
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

# 修改数据方法
'''
1. 支持未知ID单条数据修改
    URL:    /xxx/first
    DATA:   {...}
    此方法会找数据库第一条数据，进行对应修改，用于特殊用途
2. 支持单ID数据修改
    URL: /xxx/:id
    DATA:   {...}
    正常使用，数据为需要修改的数据字典
3. 支持多ID单数据修改
    URL: /xxx/1,2,3,4,5,6
    DATA:   {...}
    支持将多条数据的内容进行统一处理，例如批量加入回收站或者批量转移归属栏目等
4. 支持多ID多数据修改
    URL: /xxx/batch
    DATA:   {'data': [{...}, {...}, {...}, {...}]}
    将需要多条修改的数据构成数组，用 'data' 字段传进来。
    每个数据里面必须包含 'id' 字段，否则参数错误
'''
def put(className, oid, data):
    if not hasClass(className):
        return 404

    # 构建成功和失败 id 数据
    succIds = []
    failIds = []

    # 修改数据方法
    def putData(res, id, dat = data):
        if res:
            oldData = getDict(res)
            for i in dat:
                setattr(res, i, dat[i])

            session.add(res)
            session.commit()
            succIds.append(oldData['id'])
        else:
            failIds.append(id)

    # 检查提交数据是否符合表要求方法
    def checkField(dat, fields):
        for i in dat:
            if not i in fields:
                return 400
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)

        fields = getFieldList(classModel)

        # 处理不知道ID的单条数据修改
        if oid == 'first':
            checkField(data, fields)
            putData(res.first(), -1)
        # 处理多条数据批量修改
        elif oid == 'batch':
            if not data.get('data'):
                return 400
            dat = data['data']
            for i in dat:
                checkField(i, fields)
                if not i.get('id'):
                    return 400
            for i in dat:
                putData(res.get(i['id']), i['id'], i)

        # 处理正常单条数据单ID或多ID批量修改
        else:
            checkField(data, fields)
            idArr = oid.split(',')
            for id in idArr:
                putData(res.get(id), int(id))

        if len(succIds) == 0:
            return 400
        else:
            return {'success': succIds, 'fail': failIds}

    except Exception as e:
        return 503

# 删除数据方法
'''
支持多条数据删除，多条数据删除只需要传多个ID参数即可
单条示例 xxx/1
多条示例 xxx/1,2,3,4,5
返回结果为一个对象，包含俩数组
success 返回成功删除的的id序列
fail 返回删除失败的id序列
如果成功列表长度为 0 则返回参数错误
'''
def delete(className, oid):
    if not hasClass(className):
        return 404
    idArr = oid.split(',')
    succIds = []
    failIds = []
    try:
        classModel = getattr(model, className)
        for i in idArr:
            res = session.query(classModel).get(i)
            if res:
                session.delete(res)
                session.commit()
                succIds.append(i)
            else:
                failIds.append(i)
        if len(succIds) == 0:
            return 400
        else:
            return {'success': succIds, 'fail': failIds}
    except Exception as e:
        return 503
