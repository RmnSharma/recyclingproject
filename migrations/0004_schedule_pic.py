# Generated by Django 2.0 on 2021-08-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_apt'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='pic',
            field=models.ImageField(default='', upload_to='img/'),
        ),
    ]