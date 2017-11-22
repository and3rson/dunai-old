# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('photo', models.ImageField(upload_to='photos')),
                ('comment', models.TextField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
