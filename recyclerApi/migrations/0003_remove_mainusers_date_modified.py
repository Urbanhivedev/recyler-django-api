# Generated by Django 3.0.4 on 2020-03-26 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recyclerApi', '0002_auto_20200326_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainusers',
            name='date_modified',
        ),
    ]
