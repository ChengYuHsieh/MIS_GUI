# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20150923_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='airlineagreement',
            name='startCtrTime',
            field=models.IntegerField(default=120),
        ),
        migrations.AddField(
            model_name='flight',
            name='destination',
            field=models.CharField(default='Taiwan', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='flightRoute',
            field=models.CharField(default='Asia', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='origin',
            field=models.CharField(default='Japan', max_length=30),
            preserve_default=False,
        ),
    ]
