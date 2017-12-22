#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
##########################################################################
# Name:    seepw.py                                                      #
# Author:  FungLeo                                                       #
# Date:    2017-12-20                                                    #
# Purpose: used to manage the password saved in the database             #
# Copy:    for study, prohibition of commercial use                      #
##########################################################################
import db
import argparse
from pwlang import lang

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description=lang('seepw_desc')
    parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--id", help=lang('seepw_id'))
    group.add_argument("-n", "--name", help=lang('seepw_name'))
    group.add_argument("-d", "--delete", help=lang('seepw_dele'))
    args = parser.parse_args()
    name = args.name if args.name else False
    pId = args.id if args.id else False
    dId = args.delete
    
    if dId:
        if dId.isdigit():
            db.deleteDb(dId)
        else:
            print(lang('seepw_err_did'))
    else:
        db.selectDb(pId,name)
