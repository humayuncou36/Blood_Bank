# Generated by Django 5.1.5 on 2025-02-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_userprofile_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]
