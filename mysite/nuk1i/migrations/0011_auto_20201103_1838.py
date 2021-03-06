# Generated by Django 3.1.3 on 2020-11-03 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorietracker', '0010_auto_20201025_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfpcredentials',
            name='last_mfp_log_date_synced',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mfpcredentials',
            name='mfp_autosync',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mfpcredentials',
            name='mfp_autosync_startdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 4, 18, 38, 25, 669161)),
        ),
        migrations.AlterField(
            model_name='setting',
            name='goal_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 18, 38, 25, 671070), null=True),
        ),
    ]
