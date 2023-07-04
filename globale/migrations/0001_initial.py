# Generated by Django 4.2.1 on 2023-07-02 11:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('rang', models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('poste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globale.poste')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('nom', models.CharField(default='', max_length=30)),
                ('nature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globale.race')),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globale.client')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=255)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globale.personnel')),
            ],
        ),
    ]
