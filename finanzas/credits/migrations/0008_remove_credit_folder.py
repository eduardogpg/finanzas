# Generated by Django 3.2.10 on 2022-01-23 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0007_auto_20220110_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='folder',
        ),
    ]