import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Raj', 'Sharma', 27, 'M', 60000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
