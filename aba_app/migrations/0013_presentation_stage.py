# Generated by Django 4.1.3 on 2022-11-15 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0012_remove_stage_presentation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aba_app.stage'),
        ),
    ]
