import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database='ninja_turtles'
)

mycur = mydb.cursor()
mycur.execute('select * from turtles')
result = mycur.fetchall()
print(result)