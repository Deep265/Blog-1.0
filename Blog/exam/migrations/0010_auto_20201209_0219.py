# Generated by Django 3.1.2 on 2020-12-08 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20201115_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examans',
            name='question',
        ),
        migrations.DeleteModel(
            name='questionkey',
        ),
    ]
