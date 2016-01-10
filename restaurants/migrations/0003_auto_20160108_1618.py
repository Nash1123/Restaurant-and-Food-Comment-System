# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20160108_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='f_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='r_name',
            new_name='name',
        ),
    ]
