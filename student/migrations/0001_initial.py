# Generated by Django 3.1.5 on 2021-01-26 12:14

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testNo', models.PositiveIntegerField()),
                ('chinese', models.DecimalField(decimal_places=2, max_digits=3, validators=[student.models.validateGrade])),
                ('english', models.DecimalField(decimal_places=2, max_digits=3, validators=[student.models.validateGrade])),
                ('math', models.DecimalField(decimal_places=2, max_digits=3, validators=[student.models.validateGrade])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20, validators=[student.models.validatePhone])),
            ],
        ),
    ]
