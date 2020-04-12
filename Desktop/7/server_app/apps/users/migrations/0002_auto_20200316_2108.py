# Generated by Django 2.2.6 on 2020-03-16 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(help_text='关联用户类型', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='students', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='姓名')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('user', models.OneToOneField(help_text='关联用户类型', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teachers', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='姓名')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='admtype',
            name='user',
            field=models.OneToOneField(help_text='关联管理员类型', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admins', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_server_man',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
