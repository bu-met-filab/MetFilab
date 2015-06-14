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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org', models.CharField(max_length=50)),
                ('intro', models.TextField(max_length=300)),
                ('topic', models.CharField(max_length=100, null=True, blank=True)),
                ('reason', models.TextField(max_length=300)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Applied'), (b'V', b'Approved'), (b'R', b'Rejected')])),
                ('reject_reason', models.TextField(max_length=300, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
