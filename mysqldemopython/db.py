import mysql.connector

con = mysql.connector.connect(
    host = "d.takeshi",
    user= "root",
    password = "password",
    database = "takeshi",
    port = 3306
)

printI("Hey, I think i am connected!")

con.close()