# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DutySkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='duty',
            name='femaleDemand',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='duty',
            name='maleDemand',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dutyskill',
            name='dutyID',
            field=models.ForeignKey(to='database.Duty'),
        ),
        migrations.AddField(
            model_name='dutyskill',
            name='skillID',
            field=models.ForeignKey(to='database.Skill'),
        ),
        migrations.AlterUniqueTogether(
            name='dutyskill',
            unique_together=set([('dutyID', 'skillID')]),
        ),
    ]
