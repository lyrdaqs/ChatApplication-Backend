# Generated by Django 3.2 on 2021-06-03 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_user_contacts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
