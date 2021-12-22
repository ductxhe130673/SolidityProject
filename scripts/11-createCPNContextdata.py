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
    ("EtherLotto Context", "<DCRModel>\n<id>220802</id>\n<title>Healthcare Workflow</title>\n<events>\n<id>play</id>\n</events>\n<events>\n<id>claimReward</id>\n</events>\n<rules>\n<type>condition</type>\n<source>play</source>\n<target>claimReward</target>\n</rules>\n<rules>\n<type>include</type>\n<source>claimReward</source>\n<target>play</target>\n</rules>\n</DCRModel>","DCR",datetime.datetime.now(),"This is desciption","1"),
    ("blindAuction Context", "<DCRModel>\n<id>220802</id>\n<title>Healthcare Workflow</title>\n<events>\n<id>play</id>\n</events>\n<events>\n<id>claimReward</id>\n</events>\n<rules>\n<type>condition</type>\n<source>play</source>\n<target>claimReward</target>\n</rules>\n<rules>\n<type>include</type>\n<source>claimReward</source>\n<target>play</target>\n</rules>\n</DCRModel>","DCR",datetime.datetime.now(),"This is desciption","1"),
    ("EtherGame Context", "<DCRModel>\n<id>220802</id>\n<title>Healthcare Workflow</title>\n<events>\n<id>play</id>\n</events>\n<events>\n<id>claimReward</id>\n</events>\n<rules>\n<type>condition</type>\n<source>play</source>\n<target>claimReward</target>\n</rules>\n<rules>\n<type>include</type>\n<source>claimReward</source>\n<target>play</target>\n</rules>\n</DCRModel>","CPN",datetime.datetime.now(),"This is desciption","1"),
]
mycursor.executemany(sqlFomular,multi)
db.commit()
