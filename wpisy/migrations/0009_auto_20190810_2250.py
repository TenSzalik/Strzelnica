# Generated by Django 2.0.7 on 2019-08-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0008_auto_20190810_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wpis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(default='', max_length=200)),
                ('strzelec', models.CharField(choices=[('G', 'Gracjan'), ('K', 'Konrad'), ('W', 'Wąż'), ('B', 'Bestia'), ('J', 'Jagoda'), ('R', 'Rafał')], max_length=1)),
                ('data', models.DateField()),
                ('punkty', models.IntegerField()),
                ('oddane_strzaly', models.IntegerField()),
                ('dystans', models.IntegerField(default=10)),
                ('rodzaj_tarczy', models.CharField(choices=[('Ł', 'Łatwa'), ('Ś', 'Średnia'), ('T', 'Trudna')], default='Trudna', max_length=1)),
                ('opis', models.TextField(default='Nihil novi')),
            ],
            options={
                'verbose_name_plural': 'Wpis',
            },
        ),
        migrations.DeleteModel(
            name='Strzelansko',
        ),
    ]