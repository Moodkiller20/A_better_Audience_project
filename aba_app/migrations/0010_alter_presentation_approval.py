# Generated by Django 4.1.3 on 2022-11-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0009_alter_presentation_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='approval',
            field=models.CharField(choices=[('APPROVE', 'APPROVED'), ('DECLINE', 'DECLINED'), ('UNAPPROVED', 'UNAPPROVED')], default=('UNAPPROVED', 'UNAPPROVED'), max_length=15),
        ),
    ]
