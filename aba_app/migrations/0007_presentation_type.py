# Generated by Django 4.1.3 on 2022-11-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0006_stage_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='type',
            field=models.CharField(blank=True, choices=[('Teaching', 'Teaching'), ('Providing Information', 'Providing Information'), ('Reporting Progress', 'Reporting Progress'), ('Marketing', 'Marketing'), ('Solving a Problem', 'Solving a Problem'), ('Class Presentation', 'Class Presentation')], max_length=50, null=True),
        ),
    ]
