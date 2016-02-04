# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20160204_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Forward'), (b'M', b'Midfielder'), (b'D', b'Defenseman'), (b'G', b'Goalie')]),
        ),
    ]
