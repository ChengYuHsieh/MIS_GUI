# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20150917_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='numCIQC',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='numCIQF',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='numCIQOther',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='numCIQY',
        ),
    ]
