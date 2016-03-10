# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-11 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0020_remove_task_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagTaskMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Keyword')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Task')),
            ],
        ),
    ]