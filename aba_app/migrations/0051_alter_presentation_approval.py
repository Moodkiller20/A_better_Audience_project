# Generated by Django 4.1.3 on 2022-12-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0050_alter_presentation_pres_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='approval',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Declined', 'Declined'), ('Unapproved', 'Unapproved')], default='Unapproved', max_length=50, null=True),
        ),
    ]
