# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20151008_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalSchedule',
            fields=[
                ('employeeID', models.ForeignKey(primary_key=True, serialize=False, to='database.Employee')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('schedule', models.ForeignKey(to='database.SeasonalSchedule')),
            ],
        ),
    ]
