from django.db import connection
# Get Contact by Account id
def getContactByAid(id):
    try:
        sql = '''select * from Contact where aid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql,[id])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "id":row[0],
                "firstname":row[1],
                "lastname":row[2],
                "email":row[3],
                "phone":row[4],
                "birthDate":row[5],
                #"avartar": row[6],
                "address":row[7]
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
        cursor.execute(sql,[author_id])
        avartar = cursor.fetchone()[0]
        #onn = MySQLConnection(**db_config)
        #cursor = conn.cursor()
        #cursor.execute(sql, (author_id,))
        #photo = cursor.fetchone()[0]

        # write blob data into a file
        write_file(avartar, filename)
        return True

    except Exception as e:
        print("ERROR ==== ",e)

    finally:
        cursor.close()
        connection.close()