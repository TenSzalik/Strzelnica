# Generated by Django 2.0.7 on 2019-08-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0022_delete_wpisttt'),
    ]

    operations = [
        migrations.AddField(
            model_name='wpis',
            name='title',
            field=models.CharField(default='d', max_length=200),
        ),
    ]