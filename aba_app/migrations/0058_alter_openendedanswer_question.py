# Generated by Django 4.1.4 on 2022-12-14 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0057_openendedquestion_openendedanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openendedanswer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aba_app.openendedquestion'),
        ),
    ]
