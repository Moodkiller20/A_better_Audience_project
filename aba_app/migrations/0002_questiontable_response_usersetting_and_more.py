# Generated by Django 4.1.3 on 2022-11-15 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aba_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=60)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('ques_description', models.TextField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('ques_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=60)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aba_app.questiontable')),
                ('res_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default=None, max_length=250, null=True, upload_to='User_file/Profile_picture/')),
                ('theme', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='rub_owner',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='rubric',
        ),
        migrations.AddField(
            model_name='presentation',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='pres_description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='pres_file',
            field=models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='presentation_files/'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='pres_image',
            field=models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='Presentation_images/'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='pres_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='Stage_image',
            field=models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='stage_images/'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='stage_description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='stage_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='stage_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stage',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Rubric',
        ),
    ]
