# Generated by Django 4.1.3 on 2022-12-04 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0047_remove_questionflow_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='pres_reviewed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aba_app.presentation'),
        ),
    ]
