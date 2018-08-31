# Generated by Django 2.1.1 on 2018-08-31 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_student', models.IntegerField(default=1, verbose_name='is_student')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='last_name')),
                ('bio', models.CharField(blank=True, max_length=100, null=True, verbose_name='status')),
                ('points', models.IntegerField(default=0, verbose_name='points')),
                ('rank', models.IntegerField(default=0, verbose_name='rank')),
                ('gender', models.CharField(blank=True, max_length=7, null=True, verbose_name='gender')),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user_info',
                'managed': True,
            },
        ),
    ]
