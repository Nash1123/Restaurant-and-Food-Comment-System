# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20160109_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=255)),
                ('visitor', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('food', models.ForeignKey(to='restaurants.Food')),
            ],
            options={
                'ordering': ['date_time'],
                'permissions': (('can_comment', 'Can comment'),),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='food',
            name='comment',
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
