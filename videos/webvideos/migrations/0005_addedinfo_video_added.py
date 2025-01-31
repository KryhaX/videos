# Generated by Django 5.1.5 on 2025-01-29 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webvideos', '0004_alter_video_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField(choices=[(4, 'Drama'), (0, 'Other'), (1, 'Horror'), (3, 'Sci-Fi'), (2, 'Comedy')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='added',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webvideos.addedinfo'),
        ),
    ]
