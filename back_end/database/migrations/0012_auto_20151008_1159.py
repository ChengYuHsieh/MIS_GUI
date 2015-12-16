# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20150924_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedDuty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('dutyID', models.ForeignKey(to='database.Duty')),
                ('employeeID', models.ForeignKey(to='database.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonalSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.CharField(max_length=30)),
                ('isAgent', models.BooleanField()),
                ('startTime', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), size=100)),
                ('classType', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), size=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('assignedAirline', models.ForeignKey(to='database.Airline')),
                ('group', models.ForeignKey(to='database.Group')),
            ],
        ),
        migrations.AlterField(
            model_name='flight',
            name='numPassengerC',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='numPassengerF',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='numPassengerY',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
