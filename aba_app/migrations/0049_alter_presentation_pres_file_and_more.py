# Generated by Django 4.1.3 on 2022-12-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0048_answer_pres_reviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='pres_file',
            field=models.FileField(blank=True, default='stage_images/logo.png', max_length=250, null=True, upload_to='presentation_files/'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='pres_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Presentation_images/'),
        ),
    ]