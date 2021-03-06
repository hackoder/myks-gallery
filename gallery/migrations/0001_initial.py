# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 08:28
from __future__ import unicode_literals

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
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('dirpath', models.CharField(max_length=200, verbose_name='directory path')),
                ('date', models.DateField()),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'verbose_name': 'Album',
                'ordering': ('date', 'name', 'dirpath', 'category'),
            },
        ),
        migrations.CreateModel(
            name='AlbumAccessPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=False, verbose_name='is public')),
                ('inherit', models.BooleanField(default=True, verbose_name='photos inherit album access policy')),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='access_policy', to='gallery.Album')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='authorized groups')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='authorized users')),
            ],
            options={
                'verbose_name_plural': 'Album access policies',
                'verbose_name': 'Album access policy',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100, verbose_name='file name')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album')),
            ],
            options={
                'verbose_name_plural': 'Photos',
                'verbose_name': 'Photo',
                'ordering': ('date', 'filename'),
                'permissions': (('view', 'Can see all photos'), ('scan', 'Can scan the photos directory')),
            },
        ),
        migrations.CreateModel(
            name='PhotoAccessPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=False, verbose_name='is public')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='authorized groups')),
                ('photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='access_policy', to='gallery.Photo')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='authorized users')),
            ],
            options={
                'verbose_name_plural': 'Photo access policies',
                'verbose_name': 'Photo access policy',
            },
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('dirpath', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='photo',
            unique_together=set([('album', 'filename')]),
        ),
    ]
