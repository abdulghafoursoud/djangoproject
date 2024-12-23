# Generated by Django 5.1.4 on 2024-12-22 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crsapp', '0011_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='project',
            name='st_reg_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crsapp.student', unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
