# Generated by Django 3.1.2 on 2020-11-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=3000)),
                ('option1', models.CharField(max_length=3000)),
                ('option2', models.CharField(max_length=3000)),
                ('option3', models.CharField(max_length=3000)),
                ('option4', models.CharField(max_length=3000)),
                ('correct', models.CharField(max_length=3000)),
            ],
        ),
    ]
