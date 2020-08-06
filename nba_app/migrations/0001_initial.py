# Generated by Django 3.1 on 2020-08-05 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('teamname', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('playername', models.CharField(max_length=150)),
                ('points', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('rebounds', models.IntegerField(default=0)),
                ('blocks', models.IntegerField(default=0)),
                ('steals', models.IntegerField(default=0)),
                ('games_played', models.IntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='nba_app.team')),
            ],
        ),
    ]
