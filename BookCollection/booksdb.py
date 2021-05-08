#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:13:56 2021

@author: mdshadanaltmash
"""


from mysql_config import dbconfig
import mysql.connector as mcp
from tkinter import messagebox

conn=mcp.connect(**dbconfig)

class Bookdb:
    def __init__(self):
        self.conn=mcp.connect(**dbconfig)
        self.curr=conn.cursor()
        print(f"Connected to '{dbconfig['database'].upper()}' database ")
        
    def __del__(self):
        self.conn.close()
        
    def view(self):
        self.curr.execute('Select * from book_dtls;')
        rows=self.curr.fetchall()
        return rows
    
    def insert(self,title,author,genre,sgenre,height,pub):
        query="insert into book_dtls (title,author,genre,sub_genre,height,publisher) values (%s,%s,%s,%s,%s,%s)"
        values=[title,author,genre,sgenre,height,pub]
        self.curr.execute(query,values)
        conn.commit()
        messagebox.showinfo(title="Book Database",message="New Book Added in the database")
        
    def update(self,id,title,author,genre,sgenre,height,pub):
        query="update book_dtls set title=%s , author=%s, genre=%s, sub_genre=%s, height=%s, publisher=%s where id= %s"
        values=[title,author,genre,sgenre,height,pub,id]
        self.curr.execute(query,values)
        conn.commit()
        messagebox.showinfo(title='Book Database',message='Book Details updated')
        
    def delete(self,id):
        query="Delete from book_dtls where id=%s"
        self.curr.execute(query,[id])
        conn.commit()
        messagebox.showinfo(title='Book Databse',message='Record Deleted')
        







