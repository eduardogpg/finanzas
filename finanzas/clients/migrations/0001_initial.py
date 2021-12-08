# Generated by Django 3.2.10 on 2021-12-08 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('curp', models.CharField(max_length=18)),
                ('DNI', models.CharField(max_length=50)),
                ('marital_status', models.CharField(max_length=200)),
                ('spouse', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('children', models.IntegerField(default=0)),
            ],
        ),
    ]
