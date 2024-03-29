# Generated by Django 3.2.5 on 2021-07-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0015_auto_20210718_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
    ]
