# Generated by Django 3.0.6 on 2020-05-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20200515_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default='203 Fake St. Mountain View, San Francisco, California, USA', max_length=300),
            preserve_default=False,
        ),
    ]
