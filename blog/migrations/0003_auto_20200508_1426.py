# Generated by Django 3.0.6 on 2020-05-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='new_field',
        ),
        migrations.AddField(
            model_name='post',
            name='content_preview',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
