# Generated by Django 4.1.3 on 2022-11-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0033_remove_presentation_approval'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='evalution_owner',
            new_name='evaluation_owner',
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='evaluation',
            field=models.IntegerField(blank=True, max_length=60, null=True),
        ),
    ]
