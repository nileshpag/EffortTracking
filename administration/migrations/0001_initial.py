# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pull_request', models.IntegerField(max_length=5)),
                ('review_type', models.CharField(choices=[('peer', 'Peer'), ('client', 'Client'), ('qa', 'QA')], max_length=30)),
                ('filename', models.TextField()),
                ('comment', models.TextField()),
                ('review_date', models.DateTimeField()),
                ('fix_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('peer', 'Peer'), ('client', 'Client'), ('qa', 'QA')], max_length=30)),
                ('rca', models.CharField(choices=[('domo_standard', 'DOMO Standard'), ('angularjs_exp', 'AngularJS Experience'), ('client_code', 'Client Code'), ('enhancement', 'Enhancement'), ('code_optimization', 'Code Optimization'), ('requirement_conflict', 'Requirement Conflict'), ('reviewer_conflict', 'Reviewer Conflict'), ('appreciation', 'Appreciation')], max_length=30)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developer', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Code Review Records',
                'ordering': ['-developer'],
            },
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprint_name', models.CharField(max_length=30)),
                ('sprint_start_date', models.DateTimeField(editable=False)),
                ('sprint_end_date', models.DateTimeField(editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sprint',
                'ordering': ['-sprint_name'],
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask_id', models.CharField(max_length=10)),
                ('subtask_scope', models.CharField(choices=[('planned', 'Planned'), ('unplanned', 'Unplanned')], max_length=20)),
                ('status', models.CharField(choices=[('development', 'Development'), ('peer_review', 'Unplanned'), ('internal_qa', 'Internal QA'), ('pull_request', 'Pull Request'), ('client_review', 'Client Review'), ('review_fix', 'Review Fix'), ('merged', 'Merged'), ('qa_testing', 'QA Testing'), ('closed', 'Closed'), ('blocked', 'Blocked'), ('next_sprint', 'Next Sprint'), ('assigned_to_client', 'Assigned to Client'), ('infra_process', 'Infra Process')], max_length=20)),
                ('team', models.CharField(choices=[('WETL', 'WETL'), ('Matrix', 'Matrix'), ('Gambit', 'Gambit'), ('Goonies', 'Goonies')], max_length=20)),
                ('effort', models.IntegerField(max_length=2)),
                ('assigned_datetime', models.DateTimeField(editable=False)),
                ('created_datetime', models.DateTimeField(editable=False)),
                ('modified_datetime', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Sub Task',
                'ordering': ['-subtask_id'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=10)),
                ('story_point', models.IntegerField(max_length=2)),
                ('created_datetime', models.DateTimeField(editable=False)),
                ('modified_datetime', models.DateTimeField()),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Sprint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'ordering': ['-task_id'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(choices=[('developer', 'Developer'), ('qa', 'QA')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Task'),
        ),
        migrations.AddField(
            model_name='subtask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='codereview',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Sprint'),
        ),
        migrations.AddField(
            model_name='codereview',
            name='subtask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.SubTask'),
        ),
    ]
