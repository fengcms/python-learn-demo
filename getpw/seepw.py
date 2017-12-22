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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description='This program is used to manage the password saved in the database'
    parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--id", help="The ID of the password you want to look at")
    group.add_argument("-n", "--name", help="The NAME of the password you want to look at")
    group.add_argument("-d", "--delete", help='Delete mode, the parameter is ID')
    args = parser.parse_args()
    name = args.name if args.name else False
    pId = args.id if args.id else False
    dId = args.delete
    
    if dId:
        if dId.isdigit():
            db.deleteDb(dId)
        else:
            print('Error: The parameters of the delete mode must be number')
    else:
        db.selectDb(pId,name)
