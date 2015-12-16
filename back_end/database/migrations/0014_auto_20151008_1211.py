# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_personalschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalschedule',
            name='employeeID',
            field=models.OneToOneField(primary_key=True, serialize=False, to='database.Employee'),
        ),
    ]
