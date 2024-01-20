# Generated by Django 5.0.1 on 2024-01-20 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0009_alter_department_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cin', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('department_name', models.CharField(max_length=100)),
                ('cadre', models.CharField(max_length=255)),
                ('adresse', models.CharField(blank=True, max_length=255)),
                ('phoneNumber', models.CharField(blank=True, max_length=15)),
                ('datebirth', models.DateField(blank=True, null=True)),
                ('ImageProfil', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('first_check', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.department')),
            ],
        ),
    ]
