# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20150916_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='ID',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=b'N/A', max_length=30),
        ),
        migrations.AlterField(
            model_name='group',
            name='code',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
