# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20150917_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinratioc',
            name='id',
        ),
        migrations.RemoveField(
            model_name='checkinratiof',
            name='id',
        ),
        migrations.RemoveField(
            model_name='checkinratiog',
            name='id',
        ),
        migrations.RemoveField(
            model_name='checkinratioy',
            name='id',
        ),
        migrations.AlterField(
            model_name='checkinratioc',
            name='name',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='checkinratiof',
            name='name',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='checkinratiog',
            name='name',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='checkinratioy',
            name='name',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
