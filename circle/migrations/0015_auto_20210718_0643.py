# Generated by Django 3.2.5 on 2021-07-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0014_auto_20210717_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]