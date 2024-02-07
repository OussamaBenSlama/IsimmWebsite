# Generated by Django 5.0.1 on 2024-02-03 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0015_groupe_rank'),
        ('studentsApp', '0005_student_first_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='groupTD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.groupe'),
        ),
    ]