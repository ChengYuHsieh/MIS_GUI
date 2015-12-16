# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('code', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AirlineAgreement',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('minNumCTR', models.IntegerField(default=0)),
                ('minNumCIQ', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlackListAirline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('airline', models.ForeignKey(to='database.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='BlackListEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckInRatioC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('min240', models.FloatField(default=0.0)),
                ('min210', models.FloatField(default=0.0)),
                ('min180', models.FloatField(default=0.0)),
                ('min150', models.FloatField(default=0.0)),
                ('min120', models.FloatField(default=0.0)),
                ('min90', models.FloatField(default=0.0)),
                ('min60', models.FloatField(default=0.0)),
                ('min30', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckInRatioF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('min240', models.FloatField(default=0.0)),
                ('min210', models.FloatField(default=0.0)),
                ('min180', models.FloatField(default=0.0)),
                ('min150', models.FloatField(default=0.0)),
                ('min120', models.FloatField(default=0.0)),
                ('min90', models.FloatField(default=0.0)),
                ('min60', models.FloatField(default=0.0)),
                ('min30', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckInRatioG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('min240', models.FloatField(default=0.0)),
                ('min210', models.FloatField(default=0.0)),
                ('min180', models.FloatField(default=0.0)),
                ('min150', models.FloatField(default=0.0)),
                ('min120', models.FloatField(default=0.0)),
                ('min90', models.FloatField(default=0.0)),
                ('min60', models.FloatField(default=0.0)),
                ('min30', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckInRatioY',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('min240', models.FloatField(default=0.0)),
                ('min210', models.FloatField(default=0.0)),
                ('min180', models.FloatField(default=0.0)),
                ('min150', models.FloatField(default=0.0)),
                ('min120', models.FloatField(default=0.0)),
                ('min90', models.FloatField(default=0.0)),
                ('min60', models.FloatField(default=0.0)),
                ('min30', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('jobID', models.IntegerField(default=0)),
                ('HRDemand', models.IntegerField(default=0)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('ID', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('terminal', models.CharField(max_length=30)),
                ('jobLevel', models.CharField(max_length=30)),
                ('salaryLevel', models.CharField(max_length=30)),
                ('contractType', models.CharField(max_length=30)),
                ('isFixed', models.BooleanField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('assignedAirline', models.ForeignKey(to='database.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('employeeID', models.ForeignKey(to='database.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flightNum', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('modelNumF', models.IntegerField(default=0)),
                ('modelNumC', models.IntegerField(default=0)),
                ('modelNumY', models.IntegerField(default=0)),
                ('terminal', models.CharField(max_length=30)),
                ('counter', models.IntegerField(default=0)),
                ('flightType', models.CharField(max_length=30)),
                ('gate', models.CharField(max_length=30)),
                ('startCtrTime', models.DateTimeField()),
                ('endCtrTime', models.DateTimeField()),
                ('startBoardTime', models.DateTimeField()),
                ('endBoardTime', models.DateTimeField()),
                ('departureTime', models.DateTimeField()),
                ('numCIQF', models.IntegerField(default=0)),
                ('numCIQC', models.IntegerField(default=0)),
                ('numCIQY', models.IntegerField(default=0)),
                ('numCIQOther', models.IntegerField(default=0)),
                ('numPassengerF', models.IntegerField(default=0)),
                ('numPassengerC', models.IntegerField(default=0)),
                ('numPassengerY', models.IntegerField(default=0)),
                ('serviceLevelF', models.FloatField(default=0.0)),
                ('serviceLevelC', models.FloatField(default=0.0)),
                ('serviceLevelY', models.FloatField(default=0.0)),
                ('serviceLevelG', models.FloatField(default=0.0)),
                ('groupRatio', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('airline', models.ForeignKey(to='database.Airline')),
                ('airlineAgreement', models.ForeignKey(to='database.AirlineAgreement')),
                ('checkInRatioC', models.ForeignKey(to='database.CheckInRatioC')),
                ('checkInRatioF', models.ForeignKey(to='database.CheckInRatioF')),
                ('checkInRatioG', models.ForeignKey(to='database.CheckInRatioG')),
                ('checkInRatioY', models.ForeignKey(to='database.CheckInRatioY')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('numF', models.IntegerField(default=0)),
                ('numC', models.IntegerField(default=0)),
                ('numY', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('level', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='skill',
            unique_together=set([('name', 'level', 'priority')]),
        ),
        migrations.AddField(
            model_name='employeeskill',
            name='skillID',
            field=models.ForeignKey(to='database.Skill'),
        ),
        migrations.AddField(
            model_name='employee',
            name='group',
            field=models.ForeignKey(to='database.Group'),
        ),
        migrations.AddField(
            model_name='duty',
            name='flightID',
            field=models.ForeignKey(to='database.Flight'),
        ),
        migrations.AddField(
            model_name='duty',
            name='group',
            field=models.ForeignKey(to='database.Group'),
        ),
        migrations.AddField(
            model_name='blacklistemployee',
            name='employeeID1',
            field=models.ForeignKey(to='database.Employee'),
        ),
        migrations.AddField(
            model_name='blacklistemployee',
            name='employeeID2',
            field=models.ForeignKey(related_name='blackListEmployee2', to='database.Employee'),
        ),
        migrations.AddField(
            model_name='blacklistairline',
            name='employeeID',
            field=models.ForeignKey(to='database.Employee'),
        ),
        migrations.AlterUniqueTogether(
            name='employeeskill',
            unique_together=set([('employeeID', 'skillID')]),
        ),
        migrations.AlterUniqueTogether(
            name='blacklistemployee',
            unique_together=set([('employeeID1', 'employeeID2')]),
        ),
        migrations.AlterUniqueTogether(
            name='blacklistairline',
            unique_together=set([('employeeID', 'airline')]),
        ),
    ]
