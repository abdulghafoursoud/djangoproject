# Generated by Django 5.1.4 on 2024-12-18 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crsapp', '0003_rename_project_owner_project_student_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
    ]