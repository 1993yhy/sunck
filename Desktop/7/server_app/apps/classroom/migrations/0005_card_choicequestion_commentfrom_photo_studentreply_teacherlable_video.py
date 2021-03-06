# Generated by Django 2.2.6 on 2020-04-09 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0004_auto_20200408_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='卡片标题', max_length=64, null=True, unique=True, verbose_name='卡片标题')),
                ('comment', models.CharField(default='', help_text='卡片内容', max_length=254, verbose_name='卡片内容')),
                ('reply_type', models.IntegerField(choices=[(0, 'no'), (1, 'text'), (2, 'video'), (3, 'photo'), (4, 'customize')], default=0, help_text='回复类型', verbose_name='回复类型')),
                ('send_type', models.IntegerField(choices=[(0, 'allpeople'), (1, 'somepeople'), (2, 'allgroup'), (3, 'somegroup')], default=0, help_text='发送类型', verbose_name='发送类型')),
                ('add_time', models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间')),
                ('status', models.IntegerField(choices=[(0, 'noreply'), (1, 'replyed')], default=0, help_text='回复状态', verbose_name='回复状态')),
                ('class_id', models.ForeignKey(blank=True, help_text='关联教室', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clscard', to='classroom.ClassRoom', verbose_name='关联教室')),
            ],
            options={
                'verbose_name': '卡片信息',
                'verbose_name_plural': '卡片信息',
                'db_table': 'classcard',
            },
        ),
        migrations.CreateModel(
            name='StudentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, help_text='回复内容', max_length=254, null=True, unique=True, verbose_name='回复内容')),
                ('img_url', models.CharField(blank=True, help_text='图片地址', max_length=128, null=True, unique=True, verbose_name='图片地址')),
                ('video_url', models.CharField(blank=True, help_text='视频地址', max_length=128, null=True, unique=True, verbose_name='视频地址')),
                ('question_answer', models.CharField(blank=True, help_text='选项题答案', max_length=128, null=True, unique=True, verbose_name='选项题答案')),
                ('reply_status', models.IntegerField(choices=[(0, 'noreply'), (1, 'replyed')], default=0, help_text='回复状态', verbose_name='回复状态')),
                ('reply_time', models.DateTimeField(auto_now=True, help_text='回复时间', null=True, verbose_name='回复时间')),
                ('card_id', models.ForeignKey(blank=True, help_text='关联卡片', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clscard4', to='classroom.Card', verbose_name='关联卡片')),
                ('user', models.ForeignKey(blank=True, help_text='答题人', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clsuser4', to=settings.AUTH_USER_MODEL, verbose_name='答题人')),
            ],
            options={
                'verbose_name': '学生回复',
                'verbose_name_plural': '学生回复',
                'db_table': 'studentreply',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(blank=True, help_text='视频地址', max_length=128, null=True, unique=True, verbose_name='视频地址')),
                ('add_time', models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(blank=True, help_text='创建人', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clsuser2', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('video', models.ForeignKey(blank=True, help_text='视频集', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clscard2', to='classroom.Card', verbose_name='视频集')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
                'db_table': 'classvideo',
            },
        ),
        migrations.CreateModel(
            name='TeacherLable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_lable', models.ForeignKey(blank=True, help_text='老师标签', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tealab', to='classroom.StudentReply', verbose_name='老师标签')),
            ],
            options={
                'verbose_name': '老师标签',
                'verbose_name_plural': '老师标签',
                'db_table': 'teacherlable',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.CharField(blank=True, help_text='图片地址', max_length=128, null=True, unique=True, verbose_name='图片地址')),
                ('add_time', models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间')),
                ('imgs', models.ForeignKey(blank=True, help_text='图片集', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clscard1', to='classroom.Card', verbose_name='图片集')),
                ('user', models.ForeignKey(blank=True, help_text='创建人', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clsuser1', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '图片信息',
                'verbose_name_plural': '图片信息',
                'db_table': 'classphoto',
            },
        ),
        migrations.CreateModel(
            name='CommentFrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, help_text='评论内容', max_length=254, null=True, unique=True, verbose_name='评论内容')),
                ('parent_id', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teaparent', to='classroom.CommentFrom', verbose_name='父类目')),
                ('student_reply', models.ForeignKey(blank=True, help_text='老师标签', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacom', to='classroom.StudentReply', verbose_name='老师标签')),
                ('user', models.ForeignKey(blank=True, help_text='创建人', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clsuser5', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'db_table': 'commentfrom',
            },
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_comment', models.CharField(default='', help_text='选择题内容', max_length=254, verbose_name='选择题内容')),
                ('option1', models.CharField(blank=True, help_text='选项1', max_length=128, null=True, unique=True, verbose_name='选项1')),
                ('option2', models.CharField(blank=True, help_text='选项2', max_length=128, null=True, unique=True, verbose_name='选项2')),
                ('option3', models.CharField(blank=True, help_text='选项3', max_length=128, null=True, unique=True, verbose_name='选项3')),
                ('option4', models.CharField(blank=True, help_text='选项4', max_length=128, null=True, unique=True, verbose_name='选项4')),
                ('option5', models.CharField(blank=True, help_text='选项5', max_length=128, null=True, unique=True, verbose_name='选项5')),
                ('option6', models.CharField(blank=True, help_text='选项6', max_length=128, null=True, unique=True, verbose_name='选项6')),
                ('answer', models.CharField(blank=True, help_text='答案', max_length=128, null=True, unique=True, verbose_name='答案')),
                ('add_time', models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间')),
                ('question', models.ForeignKey(blank=True, help_text='视频集', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clscard3', to='classroom.Card', verbose_name='视频集')),
                ('user', models.ForeignKey(blank=True, help_text='创建人', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clsuser3', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '选择题信息',
                'verbose_name_plural': '选择题信息',
                'db_table': 'classchoicequestion',
            },
        ),
    ]
