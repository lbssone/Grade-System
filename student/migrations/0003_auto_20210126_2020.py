# Generated by Django 3.1.5 on 2021-01-26 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_grade_studentid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='studentId',
            new_name='student',
        ),
    ]
