# Generated by Django 2.0.7 on 2019-08-31 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0023_wpis_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wpis',
            name='title',
        ),
    ]