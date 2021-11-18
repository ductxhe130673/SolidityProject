from django.db import models

# Create your models here.

class Account(models.Model):
    aid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    password = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    role = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Account'

class  ltltemplate(models.Model):
    lteid= models.IntegerField(primary_key=True,db_column="lteid")
    name= models.CharField(max_length=200,db_column="name")
    formula=models.CharField(max_length=200, db_column="formula")
    template_type = models.CharField(max_length=200, db_column="template_type")
    createdDate = models.DateField(db_column="createdDate")
    description= models.CharField(max_length=200, db_column="description")
    aid = models.ForeignKey(Account, models.DO_NOTHING, db_column='aid')
    class Meta:
        managed = False
        db_table = 'LTLTemplate'