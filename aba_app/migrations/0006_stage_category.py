# Generated by Django 4.1.3 on 2022-11-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0005_alter_stage_presentation'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='category',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
