from django.db import connection
# GetGlobalBySCID
def getGlobalVarBySmartContractId(id):
    try:
        sql = '''select name,vartype,type,value  from GlobalVariable where sid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "name":row[0],
                "vartype":row[1],
                "type":row[2],
                "value":row[3]
            }
            afterFormat.append(element)
        return afterFormat
    except:
        return None
    finally:
        connection.close()

# Get LocalVariable by Function Id

def getLocalVarByFuncId(id):
    try:
        sql = '''select id,name,vartype,type,value from LocalVariable where fid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql,[id])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "id":row[0],
                "name":row[1],
                "vartype":row[2],
                "type":row[3],
                "value":row[4]
            }
            # print(element)
            afterFormat.append(element)
        return afterFormat
    except Exception as e:
        print(e)
        return None

#Get Function by Smart Contract Id
def getFunctionBySCId(id):
    try:
        sql = '''select fid,name,bodyContent from Functions where sid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql,[id])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "fid":row[0],
                # "name":row[1],
                # "bodyContent":row[2],
                "argument":getArgumentByFuncID(row[0]),
                "localVar":getLocalVarByFuncId(row[0])
            }
            # print(element)
            afterFormat.append(element)
        return afterFormat
    except Exception as e:
        print(e)
        return None

# Get Argument by FunctionId
def getArgumentByFuncID(id):
    try:
        sql = '''select * from Argument where fid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql,[id])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "id":row[0],
                "name":row[1],
                "vartype":row[2],
                "type":row[3],
                "value":row[4],
                "fid":row[5]
            }
            # print(element)
            afterFormat.append(element)
        return afterFormat
    except Exception as e:
        print(e)
        return None

# GetCPNContextIDByNameAndContextType
def getCPNContextIDByNameAndContextType(name,context_type):
    try:
        sql = '''SELECT * FROM cpncontext where name like '%"%s"%' and context_type like '%"%s"%';'''
        # SELECT * FROM cpncontext where name like '%a%' and context_type like '%y%'
        cursor = connection.cursor()
        cursor.execute(sql, [name],[context_type])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "cid":row[0]
            }
            afterFormat.append(element)
        return afterFormat
    except:
        return None
    finally:
        connection.close()  

# INSERT INTO INITIALMARKING
def addNewInitialMarking(num_user,IM_type):
    try:
        sql = '''INSERT INTO InitialMarking (num_user,IM_type) VALUES (%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([num_user],[IM_type]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New Successfull"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()       

# GetInitialMarkingTypeByInitialMarkingID
def getInitialMarkingTypeByInitialMarkingID(imId):
    try:
        sql = '''SELECT * FROM InitialMarking where imid = %s ;'''
        cursor = connection.cursor()
        cursor.execute(sql, [imId])
        dbData = cursor.fetchall()
        afterFormat = []
        for row in dbData:
            element = {
                "imid":row[0],
                "num_user":row[1],
                "IM_Type":row[2]
            }
            afterFormat.append(element)
        return afterFormat
    except:
        return None
    finally:
        connection.close() 

# INSERT INTO IMFunction
def addNewIMFunction(fun_name,sender_from,sender_to):
    try:
        sql = '''INSERT INTO IMFunction (fun_name,sender_from,sender_to,imid) VALUES (%s,%s,%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([fun_name],[sender_from],[sender_to],[getLastInsertIDFromInitialMarking()]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New IMFunction Successfull"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()      

# INSERT INTO IMArgument
def addNewIMArgument(arg_name,IMfrom,IMto):
    try:
        sql = '''INSERT INTO IMArgument (arg_name,IMfrom,IMto,imfid) VALUES (%s,%s,%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([arg_name],[IMfrom],[IMto],[getLastInsertIDFromIMFunction()]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New IMArgumentt Successfull"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()   


def InsertIMG(FilePath):
    with open(FilePath,"rb") as File :
        BinaryData = File.read()
    return BinaryData

# INSERT INTO LNAFILE
def addNewLNAFile(hcpnfile,propfile):
    try:
        sql = '''INSERT INTO LNAFile (hcpnfile,propfile) VALUES (%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([InsertIMG(hcpnfile)],[InsertIMG(propfile)]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New LNAFile Successfull"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()         

import datetime

# INSERT INTO CheckedBatchSC
def addNewCheckedBatchSC(aid,lnid,lteid,cid,imid,noSC,checkedDate,status,LTLformula,result):
    try:
        sql = '''INSERT INTO CheckedBatchSC (aid,lnid,lteid,cid,imid,noSC,checkedDate,status,LTLformula,result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([aid],[lnid],[lteid],[cid],[imid],[noSC],[datetime.datetime.now()],[status],[LTLformula],[result]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New CheckedBatchSC Successfull"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()  

# INSERT INTO CheckedSmartContractDetail
def addNewCheckedSmartContractDetail(sid,bid):
    try:
        sql = '''INSERT INTO CheckedSmartContractDetail (sid,bid) VALUES (%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([sid],[bid]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New CheckedSmartContractDetail Successfull"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close() 

# GET LAST INSERTED ID FROM INITIALMARKING
def getLastInsertIDFromInitialMarking():
    try:
        sql = '''SELECT imid FROM initialmarking ORDER BY imid DESC LIMIT 1;;'''
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        return row
    except:
        return None
    finally:
        connection.close()


# ADD NEW BALANCE
def addNewBalance(balanceType,blfrom,blto,blvalue,blrange):
    try:
        if balanceType == "Fixed":
            sql = '''INSERT INTO Balance (blvalue,imid) VALUES (%s,%s);'''
            cursor = connection.cursor()
            cursor.execute(sql, ([blvalue],[getLastInsertIDFromInitialMarking()]))
            row = cursor.fetchall()
            return "Add New Balance Successfull"
        if balanceType == "Random":
            sql = '''INSERT INTO Balance (blfrom,blto,imid) VALUES (%s,%s,%s);'''
            cursor = connection.cursor()
            cursor.execute(sql, ([blfrom],[blto],[getLastInsertIDFromInitialMarking()]))
            row = cursor.fetchall()
            return "Add New Balance Successfull"
        if balanceType == "Map":
            sql = '''INSERT INTO Balance (blrange,imid) VALUES (%s,%s);'''
            cursor = connection.cursor()
            cursor.execute(sql, ([blrange],[getLastInsertIDFromInitialMarking()]))
            row = cursor.fetchall()
            return "Add New Balance Successfull"        
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close() 

# GET IMFUNTIONID FROM IMFUNCTION BY INITIALMARKINGID AND FUNCTION_NAME
def getIMFunctionIDByIMIDAndFuncName(fun_name,imid):
    try:
        sql = '''select imfid from imfunction where fun_name like '%"%s"%' and imid = %s;'''
        cursor = connection.cursor()
        cursor.execute(sql, [fun_name],[imid])
        row = cursor.fetchall()
        return row
    except:
        return None
    finally:
        connection.close()

# GET LAST INSERTED ID FROM IMFUNCTION
def getLastInsertIDFromIMFunction():
    try:
        sql = '''SELECT imfid FROM IMFunction ORDER BY imfid DESC LIMIT 1;'''
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        return row
    except:
        return None
    finally:
        connection.close()



#mycursor = db.cursor()
#sqlFomular = "INSERT INTO InitialMarking (num_user,IM_type) VALUES (%s,%s)"
#multi = [
#    (10,"IM_type1"),
#    (20,"IM_type2"),
#    (30,"IM_type3"),
#    ]
#mycursor.executemany(sqlFomular,multi)
#db.commit()


