# Generated by Django 3.1.3 on 2020-11-19 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('video', models.BooleanField()),
                ('poster_path', models.CharField(max_length=100)),
                ('tmdb_id', models.IntegerField()),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.CharField(blank=True, max_length=100)),
                ('original_language', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('genre_ids', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('vote_average', models.FloatField()),
                ('overview', models.TextField()),
                ('release_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
