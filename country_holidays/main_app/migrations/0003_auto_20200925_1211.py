# Generated by Django 3.1.1 on 2020-09-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200925_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=5),
        ),
    ]
