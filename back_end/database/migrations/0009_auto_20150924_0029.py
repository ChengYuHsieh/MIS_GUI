# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20150923_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='endBoardTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='endCtrTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='startBoardTime',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='startCtrTime',
        ),
    ]
