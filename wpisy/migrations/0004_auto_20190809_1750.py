# Generated by Django 2.0.7 on 2019-08-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0003_auto_20190809_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strzelanie',
            name='pogoda',
        ),
        migrations.AddField(
            model_name='strzelanie',
            name='dystans',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='strzelanie',
            name='strzelec',
            field=models.CharField(choices=[('G', 'Gracjan'), ('K', 'Konrad'), ('W', 'Wąż'), ('B', 'Bestia'), ('J', 'Jagoda'), ('R', 'Rafał')], max_length=1),
        ),
    ]
