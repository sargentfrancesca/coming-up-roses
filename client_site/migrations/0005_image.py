# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_site', '0004_mailinglist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_filename', models.CharField(max_length=100)),
                ('image_title', models.CharField(max_length=64)),
                ('image_description', models.TextField(null=True)),
                ('image_folder', models.CharField(default='photo_shoot', max_length=100)),
            ],
        ),
    ]