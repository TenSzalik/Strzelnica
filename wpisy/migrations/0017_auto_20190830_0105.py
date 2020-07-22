# Generated by Django 2.0.7 on 2019-08-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0016_remove_wpis_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wpis',
            name='opis',
        ),
        migrations.AlterField(
            model_name='wpis',
            name='strzelec',
            field=models.CharField(choices=[('Gracjan', 'Gracjan'), ('Konrad', 'Konrad'), ('Grynia', 'Grynia'), ('Bestia', 'Bestia'), ('Jagoda', 'Jagoda'), ('Hampyl', 'Hampyl')], max_length=15),
        ),
    ]
