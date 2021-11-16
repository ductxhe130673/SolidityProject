from django.db import connection

def modifyCheckedDetail(cid):
    try:
        sql = '''UPDATE soliditycpn.checkedbatchsc SET cid = NULL WHERE cid = %s'''
        cursor = connection.cursor()
        cursor.execute(sql,[cid])
        return "Update Successful"
    except:
        return "Update Fail"
    finally:
        connection.close()