# Generated by Django 3.1.2 on 2020-12-31 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0029_auto_20210101_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_res',
            name='email',
            field=models.EmailField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='student_res',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='student_res',
            name='password',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student_res',
            name='phone',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student_res',
            name='std',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]