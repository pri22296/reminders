# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0003_remove_reminder_archived'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='message',
            new_name='detail',
        ),
        migrations.AddField(
            model_name='reminder',
            name='title',
            field=models.CharField(default='default', max_length=140),
            preserve_default=False,
        ),
    ]
