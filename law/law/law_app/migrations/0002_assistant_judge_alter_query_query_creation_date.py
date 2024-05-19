# Generated by Django 5.0.6 on 2024-05-16 17:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistant',
            name='judge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='law_app.judge'),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
