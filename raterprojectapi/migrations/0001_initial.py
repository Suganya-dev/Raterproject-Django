# Generated by Django 3.1.6 on 2021-02-17 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=30)),
                ('designer', models.CharField(max_length=30)),
                ('Number_of_players', models.IntegerField()),
                ('releaseYear', models.IntegerField()),
                ('timeToPlay', models.IntegerField()),
                ('ageRec', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=75)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=70)),
                ('gamesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.games')),
                ('playerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.games')),
                ('playerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player'),
        ),
    ]
