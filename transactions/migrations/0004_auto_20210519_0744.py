# Generated by Django 3.1.7 on 2021-05-19 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_transactions_ifsc_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='bank',
            field=models.CharField(default='ssss', max_length=10),
        ),
        migrations.AddField(
            model_name='transactions',
            name='branch',
            field=models.CharField(default='dddd', max_length=18),
        ),
    ]