# Generated by Django 2.2.6 on 2020-04-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_staticphoto_uploadphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticClassPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.ImageField(blank=True, help_text='头像', max_length=1024, null=True, upload_to='StaticPhoto', verbose_name='头像')),
            ],
            options={
                'verbose_name': '静态班级图片',
                'verbose_name_plural': '静态班级图片',
            },
        ),
        migrations.AlterModelOptions(
            name='staticphoto',
            options={'verbose_name': '静态头像图片', 'verbose_name_plural': '静态头像图片'},
        ),
    ]
