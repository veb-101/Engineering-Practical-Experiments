import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
# sql = "SELECT * FROM employee WHERE SEX = 'M'"

sql = "SELECT * FROM employee"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        F_Name = row[0]
        L_Name = row[1]
        Age = row[2]
        Sex = row[3]
        Income = row[4]
        print("First Name=", F_Name, "\nLast Name=", L_Name,
              "\nAge=", Age, "\nSex=", Sex, "\nIncome=", Income)
except:
    print("Error: unable to fecth data")
db.close()
