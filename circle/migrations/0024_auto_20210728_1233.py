# Generated by Django 3.2.5 on 2021-07-28 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0023_auto_20210728_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='left',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='left', to='circle.person'),
        ),
        migrations.AddField(
            model_name='chat',
            name='right',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='right', to='circle.person'),
        ),
    ]
