# Generated by Django 3.0.8 on 2020-08-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_formtoonec'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtoonec',
            name='kol',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='formtoonec',
            name='time',
            field=models.CharField(max_length=8),
        ),
    ]
