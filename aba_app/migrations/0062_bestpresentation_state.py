# Generated by Django 4.1.4 on 2022-12-15 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0061_rename_favoritypresentation_bestpresentation'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestpresentation',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aba_app.stage'),
        ),
    ]
