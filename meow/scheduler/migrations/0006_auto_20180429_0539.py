# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-29 05:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20180429_0535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smpost',
            options={'permissions': (('add_edit_post', 'Can add and edit posts'), ('approve_copy', 'Can mark the post as approved by copy'), ('approve_online', 'Can mark the post as approved by online'))},
        ),
    ]
