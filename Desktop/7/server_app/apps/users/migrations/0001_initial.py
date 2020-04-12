# Generated by Django 2.2.6 on 2020-03-16 10:04

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=1024)),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('email', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='电子邮箱')),
                ('is_server_man', models.BooleanField(default=True)),
                ('is_adm', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'userinfo',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role_type', models.CharField(default='', max_length=128, verbose_name='角色类型')),
                ('role_name', models.CharField(default='', max_length=128, verbose_name='角色名')),
                ('role_describe', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='角色描述')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roletype', to='users.Role', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '角色信息',
                'verbose_name_plural': '角色信息',
                'db_table': 'service_role',
            },
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='验证码')),
                ('mobile', models.CharField(max_length=11, verbose_name='电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '短信验证码',
                'verbose_name_plural': '短信验证码',
            },
        ),
        migrations.CreateModel(
            name='AdmType',
            fields=[
                ('user', models.OneToOneField(help_text='关联管理员类型', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role_name', models.CharField(blank=True, choices=[('auditor', '审核人员'), ('operator', '运营人员')], default='', max_length=128, null=True, verbose_name='角色类型')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
            ],
            options={
                'verbose_name': '管理员类型',
                'verbose_name_plural': '管理员类型',
                'db_table': 'adm_type',
            },
        ),
        migrations.CreateModel(
            name='ServerUser',
            fields=[
                ('user', models.OneToOneField(help_text='关联用户类型', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='users', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('first_name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='姓氏')),
                ('last_name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('passport_number', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='护照号')),
                ('passport_photo', models.ImageField(blank=True, default='', max_length=1024, null=True, upload_to='passport_photo', verbose_name='护照照片(正面)')),
                ('visa_photo', models.ImageField(blank=True, default='', max_length=1024, null=True, upload_to='visa_status', verbose_name='签证照片(正面)')),
                ('work_place', models.CharField(blank=True, choices=[('Auckland', 'Auckland')], default='', max_length=128, null=True, verbose_name='工作地点')),
                ('address', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='住址')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
            ],
            options={
                'verbose_name': '服务者用户信息',
                'verbose_name_plural': '服务者用户信息',
                'db_table': 'service_user',
            },
        ),
        migrations.CreateModel(
            name='Role2Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_materials', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='申请材料')),
                ('training_materials', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='培训资料')),
                ('examination_content', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='考试内容')),
                ('role_state', models.IntegerField(choices=[(0, 'under review'), (1, 'Not pass'), (2, 'Certified'), (3, 'Uncertified')], default=3, verbose_name='认证状态')),
                ('role_no_pass', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='角色未通过审核原因')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Role', verbose_name='角色相关')),
                ('userinfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.ServerUser', verbose_name='用户相关')),
            ],
            options={
                'verbose_name': '角色用户关系',
                'verbose_name_plural': '角色用户关系',
                'db_table': 'service_role_userinfo',
            },
        ),
        migrations.AddField(
            model_name='role',
            name='user',
            field=models.ManyToManyField(through='users.Role2Userinfo', to='users.ServerUser'),
        ),
    ]
