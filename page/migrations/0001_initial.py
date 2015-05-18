# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('generate_date', models.DateTimeField(verbose_name=b'date generated')),
                ('type', models.CharField(max_length=16)),
                ('to', models.CharField(max_length=45, verbose_name=b'to address')),
                ('state', models.CharField(default=b'GEN', max_length=4, verbose_name=b'status', choices=[(b'GEN', b'Generating'), (b'DISP', b'Dispatched'), (b'SENT', b'Sent'), (b'FAIL', b'Failed'), (b'RTRY', b'Retrying')])),
                ('failed_count', models.PositiveSmallIntegerField(verbose_name=b'failed attempts')),
                ('sent_date', models.DateTimeField(verbose_name=b'date sent')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submit_date', models.DateTimeField(verbose_name=b'date submitted')),
                ('short_message', models.CharField(max_length=80, verbose_name=b'short message')),
                ('long_message', models.TextField(verbose_name=b'full message')),
                ('severity', models.CharField(default=b'INFO', max_length=4, choices=[(b'INFO', b'Informational'), (b'WARN', b'Warning'), (b'CRIT', b'Critical')])),
                ('hostname', models.CharField(max_length=45, blank=True)),
                ('ticket_number', models.PositiveIntegerField(null=True, verbose_name=b'ticket number', blank=True)),
                ('from_user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='page',
            field=models.ForeignKey(to='page.Page'),
        ),
    ]
