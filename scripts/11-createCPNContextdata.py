import mysql.connector
import datetime
db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = '123456',
    database="soliditycpn"
)
mycursor = db.cursor()
sqlFomular = "INSERT INTO CPNContext (name,content,context_type,createdDate,description,aid) VALUES (%s,%s,%s,%s,%s,%s)"
multi = [ 
    ("EtherLotto Context", "this is Content 1","DCR",datetime.datetime.now(),"This is desciption","1"),
    ("blindAuction Context", "This is Content 2 ","DCR",datetime.datetime.now(),"This is desciption","1"),
    ("EtherGame Context", "This is Content 3 ","CPN",datetime.datetime.now(),"This is desciption","1"),
]
mycursor.executemany(sqlFomular,multi)
db.commit()
