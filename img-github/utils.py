from sanic.response import json
import hashlib

def md(o):
    m = hashlib.md5()
    m.update(o)
    return m.hexdigest()

def ok(data):
    if type(data) == list:
        return json({"data": {"list": data}, "status": 0})
    else:
        return json({"data": data, "status": 0})


def fail(data):
    return json({"data": data, "status": 1})


def hasRole(request, rolename):
    pass


def isLogin(request):
    if request.get('user'):
        return request.get('user', {}).get('id')
    else:
        return False


def get_uuid(request):
    return request.get('uuid', '-')


def get_uid(request):
    return request.get('session').get('uid', '-')


def uuid_info(request):
    return {'uuid': request.get('uuid', '-'), 'uid': request.get('session').get('uid', '-')}
