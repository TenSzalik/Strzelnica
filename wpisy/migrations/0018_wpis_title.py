# Generated by Django 2.0.7 on 2019-08-30 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0017_auto_20190830_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='wpis',
            name='title',
            field=models.CharField(default='post', max_length=20),
        ),
    ]
