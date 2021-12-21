import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = '123456',
    database="soliditycpn"
)
pass1= "pbkdf2_sha256$260000$gN183tr5ju1po0R1JlKdcM$J/FFCiqjTHwGc5k9JnEYVXCaKRDjTP1wyM69MWvN5T4="

mycursor = db.cursor()
sqlFomular = "INSERT INTO Account (username,password,role) VALUES (%s,%s,%s)"
multi = [
    ("xuanduc",pass1,"admin"),
    ("anhtu",pass1,"admin"),
    ("honghanh",pass1,"admin"),
    ("quangvinh",pass1,"admin"),
    ("quypham",pass1,"admin"),
]
mycursor.executemany(sqlFomular,multi)
db.commit()