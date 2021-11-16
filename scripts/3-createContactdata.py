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
<<<<<<< HEAD
<<<<<<< HEAD
    ("Le","Duc Anh","anhld@fpt.edu.vn","0984268930",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),1),
    ("Le","Anh Son","sonla@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),2),
    ("Nguyen","Minh Hanh","hanhnm@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),3),
    ("Nguyen","Minh Duc","ducnm@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),4),
    ("Nguyen","Thanh Ha","hant@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),5),
    ("Tran","Van Cuong","cuongtv@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),6),
=======
    ("Le","Duc Anh","anhld@fpt.edu.vn","0984268930",datetime.datetime.now(),InsertIMG(r"D:\Demo\SolidityProject\scripts\image\index.jpeg"),str(loc),1),
    ("Le","Anh Son","sonla@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Demo\SolidityProject\scripts\image\index.jpeg"),str(loc),2),
    ("Nguyen","Minh Hanh","hanhnm@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Demo\SolidityProject\scripts\image\index.jpeg"),str(loc),3),
    ("Nguyen","Minh Duc","ducnm@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Demo\SolidityProject\scripts\image\index.jpeg"),str(loc),4),
    ("Nguyen","Thanh Ha","hant@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Demo\SolidityProject\scripts\image\index.jpeg"),str(loc),5),
    ("Tran","Van Cuong","cuongtv@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Demo\SolidityProject\scripts\image\index.jpeg"),str(loc),6),
>>>>>>> 306893983f03565afa03eee9211a703a2f9651cf
=======
    ("Le","Duc Anh","anhld@fpt.edu.vn","0984268930",datetime.datetime.now(),InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),1),
    ("Le","Anh Son","sonla@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),2),
    ("Nguyen","Minh Hanh","hanhnm@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),3),
    ("Nguyen","Minh Duc","ducnm@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),4),
    ("Nguyen","Thanh Ha","hant@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),5),
    ("Tran","Van Cuong","cuongtv@fpt.edu.vn","0123456789",datetime.datetime.now(),InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\image\index.jpeg"),str(loc),6),
>>>>>>> b2ef9eb15c56fddd0ae09143133476b9d355ae5a
]
mycursor.executemany(sqlFomular,multi)
db.commit()