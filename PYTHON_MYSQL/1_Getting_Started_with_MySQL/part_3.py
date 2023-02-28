import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database='ninja_turtles'
)

mycur = mydb.cursor()
form = 'insert into turtles (name, color, weapon, pizza, age) values (%s, %s, %s, %s, %s)'
turtle = [('raph', 'red', 'sai', True, 15), ('don', 'purp', 'bo', True, 15), ('miky', 'orng', 'nunchu', True, 15)]
mycur.execute(form, turtle)
mydb.commit()