# Generated by Django 3.0.6 on 2020-05-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='new_field',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]