#!/usr/bin/env python
# -*- coding: utf-8 -*-

# download test002.py and test002.list
#
# how to use
# python test002.py test002.list


import sys

list=[]

listname=sys.argv[1]

with open(listname, mode="r") as fp:
    list=[s.strip() for s in fp.readlines()]

'''
with open(listname,mode="r") as fp:
    _list=fp.readlines()
    for s in _list:
        list.append(s.strip())

# 上と同じ
'''

# Check write
for x in list:
    print(x)
