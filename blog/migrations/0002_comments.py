# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=300)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('post', models.ForeignKey(related_name='commentss', to='blog.Post')),
            ],
        ),
    ]
