# Generated by Django 3.1.2 on 2020-12-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_exam_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.CharField(max_length=400),
        ),
    ]
