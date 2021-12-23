import mysql.connector
import datetime
db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = '123456',
    database="soliditycpn"
)
mycursor = db.cursor()
sqlFomular = "INSERT INTO LTLTemplate (name,createdDate,formula,formula_text,template_type,description,aid) VALUES (%s,%s,%s,%s,%s,%s,%s)"
multi = [ 
    ("interger_overflow_underflow",datetime.datetime.now(), "const minThreshold = 0\nconst maxThreshold = 2147483647\nproposition outOfRange: ('variable' < minThreshold) | ('variable' > maxThreshold);\nproperty prop: G(! outOfRange);","the case where 'variable' is greater than 2147483647 or less than 0 will never happen","type0","outOfRange(x) is a proposition defining the conditions for overflow and underflow for the variable x w.r.t the range of its type which we delimit by defining lower and higher thresholds (minThreshold and maxThreshold respectively).","1"),
    ("reetrancy", datetime.datetime.now(), "template Reentrancy()","template Reentrancy()","type1","This vulnerability is related to functions that contain instructions responsible for Ether transfer.","1"),
    ("self_destruction", datetime.datetime.now(), "template SelfDestruction();","template SelfDestruction();","type2","This vulnerability is checked by detecting the presence of a test containing this.balance in the code of the inspected function","1"),
    ("timestamp_dependence", datetime.datetime.now(), "template TimestampDependence();", "template TimestampDependence();","Type3","This vulnerability is checked by detecting the presence of timestamp dependence","1"),
    ("skip_empty_string_literal", datetime.datetime.now(), "template SkipEmptyStringLiteral();","template SkipEmptyStringLiteral();","type4","This can be checked for the function calls contained in the definition of a function f by verifying that no empty string is passed as an argument (except for the last one) to any of the function calls.","1"),
    ("uninitialized_storage_variable", datetime.datetime.now(), "template UninitializedStorageVariable();","template UninitializedStorageVariable();","Type5","This can be checked for each variable x of a complex type by the LTL property.","1"),

]
mycursor.executemany(sqlFomular,multi)
db.commit()