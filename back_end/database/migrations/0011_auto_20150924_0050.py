# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20150924_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='counter',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
