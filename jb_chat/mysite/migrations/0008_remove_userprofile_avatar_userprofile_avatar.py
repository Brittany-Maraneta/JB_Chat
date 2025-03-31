# Generated by Django 5.1.6 on 2025-03-30 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_remove_avatar_skin_remove_avatar_hair_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ManyToManyField(to='mysite.avatar'),
        ),
    ]
