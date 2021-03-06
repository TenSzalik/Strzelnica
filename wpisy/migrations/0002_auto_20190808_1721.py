# Generated by Django 2.0.7 on 2019-08-08 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strzelanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('punkty', models.IntegerField()),
                ('oddane_strzaly', models.IntegerField()),
                ('pogoda', models.TextField(default='ciepło')),
                ('opis', models.TextField(default='bla bla bla')),
            ],
            options={
                'verbose_name_plural': 'Strzelanie',
            },
        ),
        migrations.CreateModel(
            name='Zawodnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Zawodnik',
            },
        ),
        migrations.RemoveField(
            model_name='wpis',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.DeleteModel(
            name='wpis',
        ),
        migrations.AddField(
            model_name='strzelanie',
            name='strzelec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpisy.Zawodnik'),
        ),
    ]
