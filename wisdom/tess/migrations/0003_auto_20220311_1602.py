# Generated by Django 2.2 on 2022-03-11 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tess', '0002_auto_20220311_1557'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myblog',
            new_name='blog',
        ),
    ]