# Generated by Django 3.2.7 on 2021-10-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_collation='utf8_general_ci', max_length=200, null=True)),
                ('password', models.CharField(blank=True, db_collation='utf8_general_ci', max_length=200, null=True)),
                ('role', models.CharField(blank=True, db_collation='utf8_general_ci', max_length=200, null=True)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Checkedbatchsc',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_collation='utf8_general_ci', max_length=200, null=True)),
                ('checkeddate', models.DateField(blank=True, db_column='checkedDate', null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'checkedbatchsc',
                'managed': False,
            },
        ),
    ]
