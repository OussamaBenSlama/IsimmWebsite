# Generated by Django 5.0 on 2023-12-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_actualite_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='category',
            field=models.CharField(choices=[('Liscence', 'Liscence'), ('Ingenieurie', 'Ingenieurie'), ('Cycle préparatoire integré', 'Cycle préparatoire integré'), ('Mastere', 'Mastere')], max_length=255),
        ),
    ]
