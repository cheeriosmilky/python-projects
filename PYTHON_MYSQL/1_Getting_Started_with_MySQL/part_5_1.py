import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database='ninja_turtles'
)

mycur = mydb.cursor()
sql = 'insert into turtles (name, color, weapon, pizza, age) values (%s, %s, %s, %s, %s)'
turt = [('t1', 'green', 'nerf gun', False, 10),
('t2', 'blue', 'nerf gun', False, 11),
('t3', 'red', 'nerf gun', False, 19),
('t4', 'grey', 'nerf gun', False, 14),
('t5', 'black', 'nerf gun', False, 15),
('t6', 'pink', 'nerf gun', False, 10),
('t7', 'purple', 'nerf gun', False, 16),
('t8', 'rainbow', 'nerf gun', False, 23),
('t9', 'brown', 'nerf gun', False, 20),
('t0', 'blue', 'nerf gun', False, 98),
]
mycur.executemany(sql, turt)
mydb.commit()
