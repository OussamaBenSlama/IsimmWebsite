# Generated by Django 4.2.3 on 2024-02-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsApp', '0006_alter_student_grouptd'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='groupe_rank',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
