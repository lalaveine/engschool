# Generated by Django 3.0.6 on 2020-05-15 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default='3 years', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='number_of_seats',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]