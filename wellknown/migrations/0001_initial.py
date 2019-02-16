# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True)),
                ('content_type', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'ordering': ('path',),
            },
        ),
    ]
