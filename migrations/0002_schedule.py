# Generated by Django 2.0 on 2021-08-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=80)),
                ('date', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
    ]
