# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('amount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FundState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('color', models.IntegerField(default=1, choices=[(0, 'Yellow'), (1, 'Green'), (2, 'Orange'), (3, 'Red')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FundType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fund',
            name='place',
            field=models.ForeignKey(to='mainapp.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fund',
            name='provider',
            field=models.ForeignKey(to='mainapp.Provider'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fund',
            name='state',
            field=models.ForeignKey(to='mainapp.FundState'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fund',
            name='types',
            field=models.ManyToManyField(to='mainapp.FundType'),
            preserve_default=True,
        ),
    ]
