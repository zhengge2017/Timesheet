# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 23:07
from __future__ import unicode_literals

import colorfield.fields
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
            name='Activity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=64)),
                ('activity_color', colorfield.fields.ColorField(default='#9900FF', max_length=18)),
                ('activity_created', models.DateField()),
                ('activity_modified', models.DateField()),
                ('activity_created_by', models.IntegerField(default=1)),
                ('activity_modified_by', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_business_name', models.CharField(default='', max_length=64, verbose_name='Business name')),
                ('client_contact_name', models.CharField(default='', max_length=64, verbose_name='Contact name')),
                ('client_phone_number', models.CharField(default='', max_length=32, verbose_name='Telephone no')),
                ('client_email', models.EmailField(default='', max_length=128, verbose_name='Email address')),
                ('client_address1', models.CharField(default='', max_length=128, verbose_name='Address')),
                ('client_address2', models.CharField(default='', max_length=128, verbose_name='Address cont')),
                ('client_postcode', models.CharField(default='', max_length=32, verbose_name='Postcode')),
                ('client_created_on', models.DateTimeField()),
                ('client_modified_on', models.DateTimeField()),
                ('client_created_by', models.IntegerField(default=1)),
                ('client_modified_by', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField(verbose_name='Event began')),
                ('end', models.DateTimeField(verbose_name='Event ended')),
                ('event_created', models.DateField()),
                ('event_modified', models.DateField()),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=64, verbose_name='Name')),
                ('project_description', models.CharField(max_length=512, verbose_name='Description')),
                ('project_color', colorfield.fields.ColorField(default='#9900FF', max_length=18, verbose_name='Color')),
                ('project_created', models.DateField()),
                ('project_modified', models.DateField()),
                ('project_created_by', models.IntegerField(default=199)),
                ('project_modified_by', models.IntegerField(default=199)),
                ('is_active', models.BooleanField(default=True)),
                ('client_id', models.ForeignKey(db_column='client_id', default=9, on_delete=django.db.models.deletion.CASCADE, to='timesheet_app.Client')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='project_id',
            field=models.ForeignKey(db_column='project_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='timesheet_app.Project'),
        ),
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
