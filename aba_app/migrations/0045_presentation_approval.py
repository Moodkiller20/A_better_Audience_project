# Generated by Django 4.1.3 on 2022-12-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0044_questionflow_answerflow'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='approval',
            field=models.CharField(blank=True, choices=[('1', 'Approved'), ('2', 'Declined'), ('3', 'Unapproved')], max_length=50, null=True),
        ),
    ]
