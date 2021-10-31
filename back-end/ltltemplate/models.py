from django.db import models

# Create your models here.
class  ltltemplate(models.Model):
    lteid= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=200)
    formula=models.TextField()
    template_type = models.CharField(max_length=200)
    description= models.TextField()

    class Meta:
        db_table = 'LTLTemplate'