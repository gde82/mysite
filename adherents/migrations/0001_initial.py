# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adherents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('join_date', models.DateTimeField(default=datetime.datetime(2015, 9, 22, 19, 32, 41, 670712, tzinfo=utc), verbose_name=b'join date')),
                ('relance_date', models.DateTimeField(default=datetime.datetime(2016, 9, 21, 19, 32, 41, 670712, tzinfo=utc), verbose_name=b'relance date')),
            ],
        ),
    ]
