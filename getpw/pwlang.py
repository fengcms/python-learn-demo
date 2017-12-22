#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
DEFAULT_LANG = 'cn'
def lang(t):
    dicts = {}
    if DEFAULT_LANG == 'en':
        dicts = {
            'getpw_desc': 'This program is used to generate simple or complex passwords',
            'getpw_leng': 'The length of the password (Default 8)',
            'getpw_name': 'Take a name for your password and Write it in  data base',
            'getpw_simp': 'The password is made up of pure numbers',
            'getpw_comm': 'The password is made up of numbers and letters (Default)',
            'getpw_diff': 'The password is made up of numbers, letters, and punctuation',
            'getpw_err_len': 'Error: The password length should be between 4-255',
            'getpw_err_name': 'Error: The length of password name should not be more than 100',
            'getpw_save': 'And the password has been saved in data base',
            'getpw_show_left': 'New Password:',
            'getpw_show_right': 'Tip: The password has been copied to the clipboard',
            'seepw_desc': 'This program is used to manage the password saved in the database',
            'seepw_id': 'The ID of the password you want to look at',
            'seepw_name': 'The NAME of the password you want to look at',
            'seepw_dele': 'Delete mode, the parameter is ID',
            'seepw_err_did': 'Error: The parameters of the delete mode must be number',
            'db_no_emp': 'Info: record is empty',
            'db_del_succ_left': 'Success: ID ',
            'db_del_succ_right': ' password has been deleted',
            'db_del_fail': 'Failure: the password was not found',
        }
    if DEFAULT_LANG == 'cn':
        dicts = {
            'getpw_desc': '本程序用来生成简单或复杂的密码。',
            'getpw_leng': '设置密码的长度(默认 8)',
            'getpw_name': '为您要保存到数据库的密码设置一个名字。',
            'getpw_simp': '密码由纯数字构成',
            'getpw_comm': '密码由数字加大小写字母构成（默认）',
            'getpw_diff': '密码由数字大小写字母以及英文标点符号构成',
            'getpw_err_len': '错误：密码的长度只能在4-255位之间',
            'getpw_err_name': '错误：设置密码名字的长度不能超过100个字',
            'getpw_save': '密码已经保存到数据库中',
            'getpw_show_left': '新密码：',
            'getpw_show_right': '提示：密码已经复制到剪切板',
            'seepw_desc': '本程序用来查看和管理数据库中的密码',
            'seepw_id': '根据ID查看密码',
            'seepw_name': '根据保存的密码名称查询密码（模糊查询）',
            'seepw_dele': '删除模式，参数为要删除的密码的ID',
            'seepw_err_did': '错误：删除模式的参数必须是数字',
            'db_no_emp': '提示：没有符合条件的记录',
            'db_del_succ_left': '成功：ID ',
            'db_del_succ_right': ' 的密码已经被删除',
            'db_del_fail': '失败：您要删除的密码不存在',
        }
    return dicts[t]
