# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-27 03:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20171109_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='also_post_to',
            field=models.ForeignKey(blank=True, help_text='This only goes down one level (i.e. no recursion)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='scheduler.Section'),
        ),
        migrations.AlterField(
            model_name='smpost',
            name='last_edit_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='smpost',
            name='pub_ready_copy_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='smpost',
            name='pub_ready_online_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='smpost',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scheduler.Section'),
        ),
    ]
