# Generated by Django 3.0.8 on 2020-08-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20200807_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtoonec',
            name='job2',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='formtoonec',
            name='kol2',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='formtoonec',
            name='time2',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.DeleteModel(
            name='MultiFormOneC',
        ),
    ]
