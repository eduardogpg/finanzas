# Generated by Django 3.2.10 on 2021-12-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
