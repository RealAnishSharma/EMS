# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 15:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsection',
            old_name='student',
            new_name='student_id',
        ),
    ]
