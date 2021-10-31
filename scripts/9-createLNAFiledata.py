import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='123456',
    database="soliditycpn"
)


def InsertIMG(FilePath):
    with open(FilePath, "rb") as File:
        BinaryData = File.read()
    return BinaryData


mycursor = db.cursor()
sqlFomular = "INSERT INTO LNAFile (hcpnfile,propfile) VALUES (%s,%s)"
multi = [
<<<<<<< HEAD
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
=======
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
>>>>>>> origin/sprint#2


]
mycursor.executemany(sqlFomular, multi)
db.commit()
