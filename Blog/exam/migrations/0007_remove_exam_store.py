# Generated by Django 3.1.2 on 2020-11-12 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20201113_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='store',
        ),
    ]