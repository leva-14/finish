# Generated by Django 3.1 on 2020-08-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='iduser',
            field=models.CharField(default='', max_length=500, verbose_name='iduser'),
        ),
    ]