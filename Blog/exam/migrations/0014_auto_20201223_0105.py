# Generated by Django 3.1.2 on 2020-12-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20201218_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='test_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tests',
            name='test_subject',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tests',
            name='test_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
