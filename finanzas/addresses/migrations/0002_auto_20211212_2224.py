# Generated by Django 3.2.10 on 2021-12-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='lat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='long',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
