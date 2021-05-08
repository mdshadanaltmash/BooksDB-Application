from mysql_config import dbconfig
import mysql.connector as mc
import csv

conn=mc.connect(**dbconfig)
curr=conn.cursor()

with open('books.csv','r') as data: 
    csv_data=csv.reader(data)
    next(csv_data)
    for row in csv_data:
        curr.execute("insert into book_dtls (title,author,genre,sub_genre,height,publisher) values (%s,%s,%s,%s,%s,%s)",row)

conn.commit()
curr.close()
print("CSV has been imported into Database")