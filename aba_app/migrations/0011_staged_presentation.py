# Generated by Django 4.1.3 on 2022-11-15 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0010_alter_presentation_approval'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staged_presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aba_app.presentation')),
                ('stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aba_app.stage')),
            ],
        ),
    ]
