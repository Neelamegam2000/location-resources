# Generated by Django 3.2 on 2021-05-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_alter_resources_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='identifier',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
