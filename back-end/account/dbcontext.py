from django.db import connection
# Get Contact by Account id


def getContactByAid(id):
    try:
        sql = '''select * from Contact where aid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "id": row[0],
                "firstname": row[1],
                "lastname": row[2],
                "email": row[3],
                "phone": row[4],
                "birthDate": row[5],
                # "avartar": row[6],
                "address": row[7]
            }
            # print(element)
            afterFormat.append(element)
        return afterFormat
    except Exception as e:
        print(e)
        return None
    finally:
        cursor.close()
        connection.close()


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


def read_blob(author_id, filename):
    # select photo column of a specific author
    sql = "SELECT avartar FROM Contact WHERE aid = %s"

    # read database configuration
    #db_config = read_db_config()

    try:
        # sql blob data form the authors table
        cursor = connection.cursor()
        cursor.execute(sql, [author_id])
        avartar = cursor.fetchone()[0]
        #onn = MySQLConnection(**db_config)
        #cursor = conn.cursor()
        #cursor.execute(sql, (author_id,))
        #photo = cursor.fetchone()[0]

        # write blob data into a file
        write_file(avartar, filename)
        return True

    except Exception as e:
        print("ERROR ==== ", e)

    finally:
        cursor.close()
        connection.close()


def getLastInsertIDFromAccount():
    try:
        sql = '''SELECT aid FROM Account ORDER BY aid DESC LIMIT 1;'''
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]
    except:
        return None
    finally:
        connection.close()


def InsertIMG(FilePath):
    with open(FilePath, "rb") as File:
        BinaryData = File.read()
    return BinaryData


def InsertIntoContact(email):
    try:
        sql = "INSERT INTO Contact (email,aid) VALUES (%s,%s)"
        aid = getLastInsertIDFromAccount()
        cursor = connection.cursor()
        cursor.execute(sql, ([email], [aid]))
        row = cursor.fetchall()
        return "Add new Contact successfully !!!"
    except Exception as e:
        print("ERROR ==== ", e)
        return None
    finally:
        cursor.close()
        connection.close()


def getContactIdByAId(aid):
    try:
        sql = '''select id from Contact where aid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql, [aid])
        row = cursor.fetchone()
        return row[0]
    except Exception as e:
        print(e)
        return None
    finally:
        cursor.close()
        connection.close()


def UpdateContactInfor(firstname, lastname, email, phone, birthdate, avartar, address, aid):
    try:
        contactIdByAid = getContactIdByAId(aid)
        sql = " UPDATE soliditycpn.contact SET firstname = %s, lastname = %s,email = %s,phone = %s,birthDate =%s,avartar = %s,address = %s WHERE id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, ([firstname], [lastname], [email], [phone], [
                       birthdate], [InsertIMG(avartar)], [address], [contactIdByAid]))
        row = cursor.fetchall()
        return "Update Contact succesfully !!!"
    except Exception as e:
        print("ERROR ==== ", e)
        return None
    finally:
        cursor.close()
        connection.close()


def CheckEmailExisted(email):
    try:
        sql = '''select email from soliditycpn.contact where email like %s;'''
        cursor = connection.cursor()
        cursor.execute(sql, [email])
        row = cursor.fetchone()
        if row is not None:
           return "Existed"
        else : 
            return "Valid"  
    except Exception as e:
        print("ERROR ==== ",e)
        return "Exception"
    finally:
        cursor.close()
        connection.close()

def CheckUserNameExisted(username):
    try:
        sql = '''select username from soliditycpn.account where username like %s;'''
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        row = cursor.fetchone()
        if row is not None:
           return "Existed"
        else : 
            return "Valid"  
    except Exception as e:
        print("ERROR ==== ",e)
        return "Exception"
    finally:
        cursor.close()
        connection.close()