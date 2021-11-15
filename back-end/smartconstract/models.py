from django.db import models

# Create your models here.

# class SmartConstract(models.Model):
#     id = models.CharField(max_length=300,primary_key=True)
#     name = models.CharField(max_length=300)
#     date_modified = models.DateTimeField()
#     type = models.CharField(max_length=300)


class Account(models.Model):
    aid = models.AutoField(primary_key=True)
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

