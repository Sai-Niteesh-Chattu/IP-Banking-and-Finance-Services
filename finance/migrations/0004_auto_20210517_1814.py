# Generated by Django 3.1.7 on 2021-05-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20210517_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='intrest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
