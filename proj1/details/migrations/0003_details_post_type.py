# Generated by Django 2.0.13 on 2019-05-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20190505_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='post_type',
            field=models.IntegerField(default=1),
        ),
    ]