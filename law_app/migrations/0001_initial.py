# Generated by Django 5.0.6 on 2024-05-16 17:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('priority_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('priority_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'priorities',
            },
        ),
        migrations.CreateModel(
            name='QueryType',
            fields=[
                ('query_type_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('query_type_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'query_types',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('assistant_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('assistant_name', models.CharField(max_length=150)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'assistants',
            },
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('judge_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('judge_name', models.CharField(max_length=150)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'judges',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('case_number', models.CharField(max_length=20)),
                ('judge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.judge')),
            ],
            options={
                'db_table': 'cases',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('query_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('query_comments', models.TextField()),
                ('query_creation_date', models.DateTimeField()),
                ('assistant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.assistant')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.case')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.judge')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.priority')),
                ('query_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.querytype')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.status')),
            ],
            options={
                'db_table': 'queries',
                'permissions': [('change_task_status', 'Can change the status of tasks'), ('change_priority', 'Can change the priority of tasks'), ('edit_comment', 'Can edit the comments of tasks'), ('change_assistant', 'Can change the assistant in charge of tasks'), ('can_create', 'Can create new tasks')],
            },
        ),
    ]