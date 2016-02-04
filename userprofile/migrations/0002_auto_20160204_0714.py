# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='login_count',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='userID',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='position',
            field=models.CharField(default=b'Forward', max_length=64, choices=[(b'FORWARD', b'Forward'), (b'MIDFIELDER', b'Midfielder'), (b'DEFENSEMAN', b'Defenseman'), (b'GOALIE', b'Goalie')]),
        ),
    ]
