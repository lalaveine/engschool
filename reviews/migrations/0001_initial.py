# Generated by Django 3.0.6 on 2020-05-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=200)),
                ('review_text', models.CharField(max_length=500)),
                ('reviewer_image', models.ImageField(upload_to='reviews')),
            ],
        ),
    ]
