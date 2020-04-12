# Generated by Django 2.2.6 on 2020-04-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_card_choicequestion_commentfrom_photo_studentreply_teacherlable_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='is_send',
            field=models.IntegerField(choices=[(0, 'send'), (1, 'save')], default=0, help_text='发送状态: 0(发送),1(保存)', verbose_name='发送状态'),
        ),
        migrations.AlterField(
            model_name='card',
            name='reply_type',
            field=models.IntegerField(choices=[(0, 'no'), (1, 'text'), (2, 'video'), (3, 'photo'), (4, 'customize')], default=0, help_text='回复类型: 0(no),1(text),2(video),3(photo),4(customize)', verbose_name='回复类型'),
        ),
        migrations.AlterField(
            model_name='card',
            name='send_type',
            field=models.IntegerField(choices=[(0, 'allpeople'), (1, 'somepeople'), (2, 'allgroup'), (3, 'somegroup')], default=0, help_text='发送类型: 0(allpeople),1(somepeople),2(allgroup),3(somegroup)', verbose_name='发送类型'),
        ),
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.IntegerField(choices=[(0, 'noreply'), (1, 'replyed')], default=0, help_text='回复状态: 0(noreply),1(replyed)', verbose_name='回复状态'),
        ),
    ]