# Generated by Django 5.1.4 on 2024-12-13 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chairperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phone_number', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('pop', models.IntegerField()),
                ('Chairperson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crsapp.chairperson')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crsapp.street')),
            ],
        ),
    ]
