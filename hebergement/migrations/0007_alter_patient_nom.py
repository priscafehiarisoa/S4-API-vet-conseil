# Generated by Django 4.2.1 on 2023-06-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hebergement', '0006_patient_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='nom',
            field=models.CharField(default='', max_length=30),
        ),
    ]
