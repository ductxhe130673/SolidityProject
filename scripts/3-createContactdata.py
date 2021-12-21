import mysql.connector
import datetime
import requests
res = requests.get('https://ipinfo.io/')
data = res.json()
city = data['city']
region = data['region']
country = data['country']
loc = city+ " " + region+ " " + country
db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = '123456',
    database="soliditycpn"
)
def InsertIMG(FilePath):
    with open(FilePath,"rb") as File :
        BinaryData = File.read()
    return BinaryData
    

mycursor = db.cursor()
sqlFomular = "INSERT INTO Contact (firstname,lastname,email,phone,birthdate,avartar,address,aid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
multi = [
    ("Truong","Xuan Duc","ductx@fpt.edu.vn","0984268930",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index1.jpeg"),str(loc),1),
    ("Le Huu","Anh Tu","tulha@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index1.jpeg"),str(loc),2),
    ("Nguyen","Hong Hanh","hanhnh@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index1.jpeg"),str(loc),3),
    ("Ha","Quang Vinh","vinhhq@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index1.jpeg"),str(loc),4),
    ("Pham","Van Quy","quypv@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index1.jpeg"),str(loc),5),
]
mycursor.executemany(sqlFomular,multi)
db.commit()