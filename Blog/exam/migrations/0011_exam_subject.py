# Generated by Django 3.1.2 on 2020-12-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20201209_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.CharField(choices=[('1', 'Physics'), ('2', 'Chemistry'), ('3', 'Maths'), ('4', 'Bio')], default=1, max_length=400),
        ),
    ]
