# Generated by Django 2.0.5 on 2022-06-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_resources_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='profile_picture',
            field=models.FileField(blank=True, upload_to='profile_picture/'),
        ),
    ]
