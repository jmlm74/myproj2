# Generated by Django 3.2.8 on 2021-10-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_utilisateurs', '0003_auto_20211012_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='util_civil',
            field=models.CharField(choices=[('Mr', 'Monsieur'), ('Mme', 'Madame'), ('Mlle', 'Mademoiselle')], max_length=4, verbose_name='Civilite'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='util_first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Prenom'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='util_phone1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='N Telephone'),
        ),
    ]
