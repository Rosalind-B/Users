# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 19:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0003_auto_20180119_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_address',
            new_name='email',
        ),
    ]