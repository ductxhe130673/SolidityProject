from django.db import connection

def modifyCheckedDetail(cid):
    try:
        sql = '''UPDATE soliditycpn.CheckedBatchSC SET lteid = NULL WHERE lteid = %s'''
        cursor = connection.cursor()
        cursor.execute(sql,[cid])
        return "Update Successful"
    except:
        return "Update Fail"
    finally:
        connection.close()