# Generated by Django 2.0.5 on 2022-04-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20210517_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_id', models.BigIntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='resources',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
