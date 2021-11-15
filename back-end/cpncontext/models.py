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

class cpncontext(models.Model):
    cid = models.AutoField(primary_key=True,db_column='cid')
    name = models.TextField(max_length=200,db_column='name')
    content = models.TextField(max_length=1000,db_column='content')
    context_type = models.TextField(max_length=200,db_column='context_type')
    description= models.TextField(max_length=700,db_column='description')
    aid = models.ForeignKey(Account, models.DO_NOTHING, db_column='aid')

    class Meta:
        managed = False
        db_table = 'CPNContext'

    
 

    