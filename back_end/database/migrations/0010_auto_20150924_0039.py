# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20150924_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='arrivalTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='checkInRatioC',
            field=models.ForeignKey(default=b'general', blank=True, to='database.CheckInRatioC', null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='checkInRatioF',
            field=models.ForeignKey(default=b'general', blank=True, to='database.CheckInRatioF', null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='checkInRatioG',
            field=models.ForeignKey(default=b'general', blank=True, to='database.CheckInRatioG', null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='checkInRatioY',
            field=models.ForeignKey(default=b'general', blank=True, to='database.CheckInRatioY', null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='counter',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departureTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='groupRatio',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='numPassengerC',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='numPassengerF',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='numPassengerY',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='serviceLevelC',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='serviceLevelF',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='serviceLevelG',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='serviceLevelY',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
    ]
