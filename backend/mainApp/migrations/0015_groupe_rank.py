# Generated by Django 5.0.1 on 2024-01-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_rename_speciality_name_groupe_formation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='rank',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
