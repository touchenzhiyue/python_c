# -*- coding:gbk -*-
# mysql数据库连接公共类
# version 1.0
# createdate 20181224

import MySQLdb

def myDB():
    db = MySQLdb.connect(host='localhost',user='root',password='chenzhiyue123',db='czy_db',charset='utf-8')

    cursor = db.cursor()
    cursor.execute("use czy_db;show tables;")

    res = cursor.fetchall()

    while res:
        print res
        res = cursor.fetchone()
    db.close()

if __name__ == "main":
    myDB()
