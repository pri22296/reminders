# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 08:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_reminder_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='archived',
        ),
    ]
