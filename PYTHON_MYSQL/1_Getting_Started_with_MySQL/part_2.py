import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database='ninja_turtles'
)

mycur = mydb.cursor()
# mycur.execute('')
mycur.execute('show tables')
for tb in mycur:
    print(tb)