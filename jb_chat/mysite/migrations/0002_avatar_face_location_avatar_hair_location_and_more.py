# Generated by Django 5.1.6 on 2025-03-25 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='face_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='avatar',
            name='hair_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='avatar',
            name='skin_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
