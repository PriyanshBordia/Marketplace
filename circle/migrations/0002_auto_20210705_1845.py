# Generated by Django 3.2.5 on 2021-07-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='mail@mail.co', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='ph_no',
            field=models.BigIntegerField(default=0, unique=True),
        ),
    ]
