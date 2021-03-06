# Generated by Django 2.2.6 on 2020-03-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20200320_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='teacher_type',
            field=models.CharField(choices=[('Dr.', ''), ('Mr.', ''), ('Miss.', ''), ('Mrs.', '')], default='Dr.', help_text='老师类型', max_length=32, verbose_name='老师类型'),
        ),
    ]
