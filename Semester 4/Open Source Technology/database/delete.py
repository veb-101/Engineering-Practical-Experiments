import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = "DELETE FROM employee WHERE Income > '%d'" % (5000)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
