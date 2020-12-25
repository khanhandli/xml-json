# -*- coding: utf-8 -*-
import pymysql 
import pymysql.cursors 
import json  
con = pymysql.connect(host='localhost', 
                      user='root', 
                      password='', 
                      db='testphp', 
                      charset='utf8mb4', 
                      cursorclass=pymysql.cursors.DictCursor)  
with con.cursor() as cur:
    # cur = con.cursor() 
    cur.execute("SELECT * FROM users") 
    rows = cur.fetchall()
    with open("data_file.json", "w") as write_file: 
        json.dump(rows, write_file)
    file = open('data_file.json','r')
    data = json.load(file)
    for p in data:
        print("Tên dang nh?p: "+p['user'])
        print("M?t kh?u :"+p['password'])
        print("")
    
    