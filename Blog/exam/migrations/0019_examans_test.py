# Generated by Django 3.1.2 on 2020-12-24 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0018_tests_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='examans',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.tests'),
        ),
    ]
