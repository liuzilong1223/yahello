# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=20)),
                ('ppwd', models.CharField(max_length=40)),
                ('pemail', models.CharField(max_length=20)),
                ('pshou', models.CharField(default=b'', max_length=10)),
                ('paddr', models.CharField(default=b'', max_length=100)),
                ('pcode', models.CharField(default=b'', max_length=6)),
                ('pphone', models.CharField(default=b'', max_length=11)),
            ],
        ),
    ]
