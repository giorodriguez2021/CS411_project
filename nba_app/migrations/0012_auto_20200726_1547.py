# Generated by Django 3.0.8 on 2020-07-26 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba_app', '0011_auto_20200726_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_id',
            new_name='player_number',
        ),
    ]