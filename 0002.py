import random
import string

import pymysql

db = pymysql.connect("localhost","root","123456","pymysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

for j in range(200):
    chars = string.digits + string.ascii_uppercase
    chosen_char = [random.choice(chars) for i in range(12)]
    promo_code = ''.join(chosen_char)
    # 使用 execute()  方法执行 SQL 查询
    sql = "insert into promo_code (promo_code) values ('{0}')".format(promo_code)
    print(sql)
    cursor.execute(sql)
    db.commit()

