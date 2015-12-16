# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20150917_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='checkInRatioC',
            field=models.ForeignKey(default=b'general', to='database.CheckInRatioC'),
        ),
        migrations.AddField(
            model_name='flight',
            name='checkInRatioF',
            field=models.ForeignKey(default=b'general', to='database.CheckInRatioF'),
        ),
        migrations.AddField(
            model_name='flight',
            name='checkInRatioG',
            field=models.ForeignKey(default=b'general', to='database.CheckInRatioG'),
        ),
        migrations.AddField(
            model_name='flight',
            name='checkInRatioY',
            field=models.ForeignKey(default=b'general', to='database.CheckInRatioY'),
        ),
    ]
