from django.db import models

# Create your models here.

class cpncontext(models.Model):
    cid = models.AutoField(primary_key=True,db_column='cid')
    name = models.TextField(max_length=200,db_column='name')
    content = models.TextField(max_length=1000,db_column='content')
    context_type = models.TextField(max_length=200,db_column='context_type')
    description= models.TextField(max_length=700,db_column='description')

    class Meta:
        managed = False
        db_table = 'CPNContext'

    
 

    