# Generated by Django 2.2 on 2022-03-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tess', '0004_auto_20220312_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='prove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('option', models.CharField(max_length=200)),
                ('sub', models.FileField(upload_to='')),
            ],
        ),
    ]
