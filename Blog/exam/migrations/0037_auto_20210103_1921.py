# Generated by Django 3.1.2 on 2021-01-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0036_testdetailview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestDetailView',
        ),
        migrations.AlterField(
            model_name='registers',
            name='time',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
