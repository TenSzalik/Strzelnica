# Generated by Django 2.0.7 on 2019-08-13 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0010_auto_20190812_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wpis',
            name='punkty',
            field=models.IntegerField(default=10),
        ),
    ]
