# Generated by Django 5.1 on 2024-09-06 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='APPOINTMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('address', models.CharField(max_length=100)),
                ('admin_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='farmapp.admin')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='farmapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='APPOINTMENT_DETAILS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.IntegerField()),
                ('condition', models.CharField(max_length=100)),
                ('recommendation', models.CharField(max_length=1000)),
                ('next_c', models.CharField(max_length=100)),
                ('admin_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_details', to='farmapp.admin')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_details', to='farmapp.user')),
            ],
        ),
    ]
