# Generated by Django 3.1.2 on 2020-10-31 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisan', '0007_auto_20201031_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='category',
            field=models.CharField(choices=[(1, 'Essentials'), (2, 'Green Vegetables'), (3, "Today's Special")], default='Essentials', max_length=10),
        ),
    ]
