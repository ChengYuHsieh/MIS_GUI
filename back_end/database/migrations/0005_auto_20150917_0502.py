# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20150917_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='checkInRatioC',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='checkInRatioF',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='checkInRatioG',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='checkInRatioY',
        ),
    ]
