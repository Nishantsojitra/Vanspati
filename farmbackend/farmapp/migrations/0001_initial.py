# Generated by Django 5.1 on 2024-08-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADMIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('passward', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ph_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('passward', models.CharField(max_length=15)),
            ],
        ),
    ]
