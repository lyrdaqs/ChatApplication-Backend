# Generated by Django 3.2 on 2021-06-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0009_auto_20210606_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
