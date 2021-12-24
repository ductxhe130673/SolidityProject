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
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"C:\Capstone\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),

=======
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
>>>>>>> origin/sprint#3
]
mycursor.executemany(sqlFomular, multi)
db.commit()
