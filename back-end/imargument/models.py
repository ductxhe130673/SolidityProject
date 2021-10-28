from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    password = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    role = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Account'

class Smartcontract(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    type = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    aid = models.ForeignKey(Account, models.DO_NOTHING, db_column='aid')

    class Meta:
        managed = False
        db_table = 'SmartContract'

class Functions(models.Model):
    fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    bodyContent = models.TextField(blank=True, null=True)
    sid = models.ForeignKey(Smartcontract, models.DO_NOTHING, db_column='sid')

    class Meta:
        managed = False
        db_table = 'Function'      

class Argument(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    vartype = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    type = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    value = models.IntegerField()
    fid = models.ForeignKey(Functions, models.DO_NOTHING, db_column='sid')

    class Meta:
        managed = False
        db_table = 'Argument'  
                

class InitialMarking(models.Model):
    imid = models.AutoField(primary_key=True)
    num_user = models.IntegerField()
    IM_type = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
   
    class Meta:
        managed = False
        db_table = 'InitialMarking'

class IMFunction(models.Model):
    imfid = models.AutoField(primary_key=True)
    fun_name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    sender_from = models.IntegerField()
    sender_to = models.IntegerField()
    imid = models.ForeignKey(InitialMarking, models.DO_NOTHING, db_column='imid')

    class Meta:
        managed = False
        db_table = 'IMFunction'       

class IMArgument(models.Model):
    imaid = models.AutoField(primary_key=True)
    arg_name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    IMfrom = models.IntegerField()
    IMto = models.IntegerField()
    imfid = models.ForeignKey(IMFunction, models.DO_NOTHING, db_column='imfid')

    class Meta:
        managed = False
        db_table = 'IMArgument'                      