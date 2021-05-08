#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:15:43 2021

@author: mdshadanaltmash
"""

import mysql.connector as mcp

conn=mcp.connect(user='sadaalt',password='qwerty',host='34.70.85.111',database='test')
cur=conn.cursor()

query1='show databases;'
op=cur.execute(query1)
print(op)