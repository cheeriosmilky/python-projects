import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database='ninja_turtles'
)

mycur = mydb.cursor()
sql = 'select * from turtles where age like %s'
mycur.execute(sql, ('%1%',))
res = mycur.fetchall()
for re in res:
    print(re)