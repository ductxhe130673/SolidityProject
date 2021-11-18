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
<<<<<<< HEAD
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"G:\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
=======
>>>>>>> 306893983f03565afa03eee9211a703a2f9651cf

    (InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
=======
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
    (InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.lna"),
     InsertIMG(r"D:\Demo\SolidityProject\scripts\XMLfile\finnal_model.prop.lna")),
>>>>>>> e8acecef1d62132ed9ec798734c4fde052285b18

]
mycursor.executemany(sqlFomular, multi)
db.commit()
