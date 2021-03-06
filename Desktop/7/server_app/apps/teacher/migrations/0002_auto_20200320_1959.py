# Generated by Django 2.2.6 on 2020-03-20 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='teacher_type',
            field=models.IntegerField(choices=[(0, '老师'), (1, '助教'), (2, '博士'), (3, '待定')], default=3, help_text='老师类型： 0（老师),1（助教),2（博士),3（待定)', verbose_name='老师类型'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='user',
            field=models.OneToOneField(help_text='老师id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teachers', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
