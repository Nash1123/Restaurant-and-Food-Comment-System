# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20160110_1956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcomment',
            options={'ordering': ['date_time'], 'permissions': (('food_can_comment', 'Food Can comment'),)},
        ),
    ]
