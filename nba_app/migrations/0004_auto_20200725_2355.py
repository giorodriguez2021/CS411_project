# Generated by Django 3.0.8 on 2020-07-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_app', '0003_auto_20200725_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_id',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
