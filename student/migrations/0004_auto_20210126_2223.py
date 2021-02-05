# Generated by Django 3.1.5 on 2021-01-26 14:23

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210126_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='chinese',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[student.models.validateGrade]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='english',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[student.models.validateGrade]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='math',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[student.models.validateGrade]),
        ),
    ]
