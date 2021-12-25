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
                "name":row[1],
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
        return "Add New InitialMarking Successfully"
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
        imid = getLastInsertIDFromInitialMarking()
        print(imid)
        sql = '''INSERT INTO IMFunction (fun_name,sender_from,sender_to,imid) VALUES (%s,%s,%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([fun_name],[sender_from],[sender_to],[imid]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New IMFunction Successfully"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()      

# INSERT INTO IMArgument
def addNewIMArgument(arg_name,IMfrom,IMto):
    try:
        imfid = getLastInsertIDFromIMFunction()
        print("imfid = ",imfid)
        sql = '''INSERT INTO IMArgument (arg_name,IMfrom,IMto,imfid) VALUES (%s,%s,%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([arg_name],[IMfrom],[IMto],[imfid]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New IMArgument Successfully"
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
        return "Add New LNAFile Successfully"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()         

import datetime

# INSERT INTO CheckedBatchSC
def addNewCheckedBatchSC(aid,lteid,cid,noSC,status,LTLformula,result):
    try:    
            sql = '''INSERT INTO soliditycpn.CheckedBatchSC (aid,lteid,cid,noSC,lnid,imid,checkedDate,status,LTLformula,result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
            cursor = connection.cursor()
            cursor.execute(sql, ([aid],[lteid],[cid],[noSC],[1],[1],[datetime.datetime.now()],[1],[LTLformula],[result]))
            row = cursor.fetchall()
            # transaction.commit()
            return "Add New CheckedBatchSC Successfully"  
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()  

# INSERT INTO CheckedSmartContractDetail
def addNewCheckedSmartContractDetail(sid):
    try:
        bid = getLastInsertIDFromCheckedBatchSC()
        sql = '''INSERT INTO CheckedSmartContractDetail (sid,bid) VALUES (%s,%s);'''
        cursor = connection.cursor()
        cursor.execute(sql, ([sid],[bid]))
        row = cursor.fetchall()
        # transaction.commit()
        return "Add New CheckedSmartContractDetail Successfully"
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close() 

# GET LAST INSERTED ID FROM INITIALMARKING
def getLastInsertIDFromInitialMarking():
    try:
        sql = '''SELECT imid FROM soliditycpn.initialmarking ORDER BY imid DESC LIMIT 1;'''
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]
    except:
        return None
    finally:
        connection.close()


# ADD NEW BALANCE
def addNewBalance(balanceType,blfrom,blto,blvalue,blrange):
    try:
        imid = getLastInsertIDFromInitialMarking()
        if balanceType == "Fixed":
            sql = '''INSERT INTO Balance (blvalue,imid) VALUES (%s,%s);'''
            cursor = connection.cursor()
            cursor.execute(sql, ([blvalue],[imid]))
            row = cursor.fetchall()
            return "Add New Balance Successfully"
        if balanceType == "Random":
            sql = '''INSERT INTO Balance (blfrom,blto,imid) VALUES (%s,%s,%s);'''
            cursor = connection.cursor()
            cursor.execute(sql, ([blfrom],[blto],[imid]))
            row = cursor.fetchall()
            return "Add New Balance Successfully"
        if balanceType == "Map":
            sql = '''INSERT INTO Balance (blrange,imid) VALUES (%s,%s);'''
            cursor = connection.cursor()
            cursor.execute(sql, ([blrange],[imid]))
            row = cursor.fetchall()
            return "Add New Balance Successfully"        
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
        row = cursor.fetchone()
        return row
    except:
        return None
    finally:
        connection.close()

# GET LAST INSERTED ID FROM IMFUNCTION
def getLastInsertIDFromIMFunction():
    try:
        sql = '''SELECT imfid FROM soliditycpn.IMFunction ORDER BY imfid DESC LIMIT 1;'''
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]
    except:
        return None
    finally:
        connection.close()

# GET LAST INSERTED ID FROM LNAFILE
def getLastInsertIDFromLNAFile():
    try:
        sql = '''SELECT lnid FROM soliditycpn.lnafile ORDER BY lnid DESC LIMIT 1;'''
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]
    except:
        return None
    finally:
        connection.close()        

# GET LAST INSERTED ID FROM CHECKEDBATCHSC
def getLastInsertIDFromCheckedBatchSC():
    try:
        sql = '''SELECT bid FROM soliditycpn.checkedbatchsc ORDER BY bid DESC LIMIT 1;'''
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]
    except:
        return None
    finally:
        connection.close() 
def updateGlobalVariable(sid):
    try:
        sql = '''UPDATE soliditycpn.globalvariable SET sid = NULL WHERE sid = %s'''
        cursor = connection.cursor()
        cursor.execute(sql,[sid])
        return "Update Successful"
    except:
        return "Update Fail"
    finally:
        connection.close()

#Update table function when delete smartcontract
def updateFunction(sid):
    try:
        sql = '''UPDATE soliditycpn.functions SET sid = NULL WHERE sid = %s'''
        cursor = connection.cursor()
        cursor.execute(sql,[sid])
        return "Update Successful"
    except:
        return "Update Fail"
    finally:
        connection.close()

#Detele checkedSmartcontractDetail
def deleteCheckedDetail(sid):
    try:
        sql = '''delete from soliditycpn.checkedsmartcontractdetail where sid = %s'''
        cursor = connection.cursor()
        cursor.execute(sql,[sid])
        return "Delete Successful"
    except:
        return "Delete Fail"
    finally:
        connection.close()