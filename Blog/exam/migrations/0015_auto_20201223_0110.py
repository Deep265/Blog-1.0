# Generated by Django 3.1.2 on 2020-12-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_auto_20201223_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='test_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
