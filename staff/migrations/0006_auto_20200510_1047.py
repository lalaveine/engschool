# Generated by Django 3.0.6 on 2020-05-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20200508_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
