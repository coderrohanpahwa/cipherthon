# Generated by Django 3.1.2 on 2020-10-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisan', '0003_auto_20201031_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
