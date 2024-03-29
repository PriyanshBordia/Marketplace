# Generated by Django 3.2.5 on 2021-07-27 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0020_auto_20210725_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/articles'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_ts',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='receiver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='circle.person'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='circle.person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile',
            field=models.ImageField(blank=True, upload_to='images/persons'),
        ),
    ]
