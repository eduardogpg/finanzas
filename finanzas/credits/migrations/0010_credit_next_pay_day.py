# Generated by Django 3.2.10 on 2022-01-24 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0009_credit_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='next_pay_day',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
