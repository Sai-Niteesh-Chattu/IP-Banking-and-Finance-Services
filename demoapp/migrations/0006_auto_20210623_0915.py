# Generated by Django 3.1.7 on 2021-06-23 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='ID',
        ),
        migrations.AddField(
            model_name='student',
            name='SID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(),
        ),
    ]
