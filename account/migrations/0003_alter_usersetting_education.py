# Generated by Django 4.1.4 on 2022-12-11 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_usersetting_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersetting',
            name='education',
            field=models.CharField(blank=True, choices=[('HS Diploma', 'HS Diploma'), ('Associate', 'Associate'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('PhD Doctoral', 'PhD Doctoral'), ('Other', 'Other')], max_length=40, null=True),
        ),
    ]
