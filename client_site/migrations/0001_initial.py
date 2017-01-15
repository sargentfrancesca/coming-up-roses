# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-14 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_name', models.CharField(max_length=30)),
                ('treatment_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_site.Category')),
            ],
        ),
    ]