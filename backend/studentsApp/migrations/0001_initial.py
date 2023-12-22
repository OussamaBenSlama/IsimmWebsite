# Generated by Django 5.0 on 2023-12-19 22:20

import django.core.validators
import studentsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(default=studentsApp.models.generate_student_id, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)])),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('cin', models.CharField(max_length=8)),
            ],
        ),
    ]
