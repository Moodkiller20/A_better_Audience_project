# Generated by Django 4.1.3 on 2022-11-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0021_criteria_evaluation_remove_response_presentation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='pres_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
