# Generated by Django 3.0.6 on 2020-05-08 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('blog', '0003_auto_20200508_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='staff.UserProfile'),
        ),
    ]
