# Generated by Django 4.1.3 on 2022-11-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0004_alter_stage_stage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='presentation',
            field=models.ManyToManyField(blank=True, null=True, to='aba_app.presentation'),
        ),
    ]