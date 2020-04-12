# Generated by Django 2.2.6 on 2020-03-18 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20200318_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('user', models.OneToOneField(help_text='关联用户类型', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teachers', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, default='', help_text='姓名', max_length=128, null=True, verbose_name='姓名')),
                ('teacher_type', models.IntegerField(choices=[(0, '老师'), (1, '助教'), (2, '博士'), (3, '待定')], default=3, help_text='老师类型', verbose_name='老师类型')),
                ('photo', models.ImageField(blank=True, help_text='老师头像', max_length=1024, null=True, upload_to='teacher_photo', verbose_name='老师头像')),
            ],
            options={
                'verbose_name': '老师信息',
                'verbose_name_plural': '老师信息',
                'db_table': 'teachers',
            },
        ),
    ]
