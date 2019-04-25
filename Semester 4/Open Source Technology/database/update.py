import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = """UPDATE employee SET Income = 8000
        WHERE First_Name = 'Raj' """

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
