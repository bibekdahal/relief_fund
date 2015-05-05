# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('items', models.ForeignKey(to='mainapp.Fund')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='FundType',
            new_name='ItemType',
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(to='mainapp.ItemType'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='fund',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='fund',
            name='types',
        ),
        migrations.AlterField(
            model_name='fund',
            name='provider',
            field=models.ForeignKey(default=None, to='mainapp.Provider', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fund',
            name='state',
            field=models.IntegerField(default=1, choices=[(0, 'Provided'), (1, 'Needed'), (2, 'Urgently Needed')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='FundState',
        ),
    ]
