# Generated by Django 3.2.10 on 2021-12-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0003_auto_20211211_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='contacte',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prospect',
            name='DNI',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='curp',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]