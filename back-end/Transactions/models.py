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

class LNAFile(models.Model):
    lnid = models.AutoField(primary_key=True)
    hcpnFile = models.TextField()
    propFile = models.TextField()

    class Meta:
        managed = False
        db_table = 'LNAFile'

class LTLTemplate(models.Model):
    lteid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    formula = models.TextField()
    template_type = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'LTLTemplate'

class CPNContext(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    content = models.TextField()
    context_type = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'CPNContext'

class InitialMarking(models.Model):
    imid = models.AutoField(primary_key=True)
    num_user = models.IntegerField()
    IM_type = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InitialMarking'

class Checkedbatchsc(models.Model):
    bid = models.AutoField(primary_key=True)
    aid = models.ForeignKey(Account, models.DO_NOTHING, db_column='aid')
    lnid = models.ForeignKey(LNAFile, models.DO_NOTHING, db_column='lnid')
    lteid = models.ForeignKey(LTLTemplate, models.DO_NOTHING, db_column='lteid')
    cid = models.ForeignKey(CPNContext, models.DO_NOTHING, db_column='cid')
    imid = models.ForeignKey(InitialMarking, models.DO_NOTHING, db_column='imid')
    noSC = models.IntegerField()
    checkeddate = models.DateField(db_column='checkedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField()
    LTLformula = models.TextField()
    result = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    
    # name = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    # description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CheckedBatchSC'