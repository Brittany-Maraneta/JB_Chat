# Generated by Django 5.1.6 on 2025-03-25 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_avatar_face_alter_avatar_hair_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.avatar'),
        ),
    ]
