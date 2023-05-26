# Generated by Django 3.2.13 on 2023-05-24 01:54

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
            name='MovieGenres',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PopularMovies',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('genres', models.CharField(blank=True, max_length=100)),
                ('release_date', models.DateField(blank=True)),
                ('popularity', models.FloatField()),
                ('vote_average', models.FloatField(default=0)),
                ('adult', models.TextField(blank=True)),
                ('poster_path', models.TextField(blank=True)),
                ('overview', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopRatedMovies',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('genres', models.CharField(blank=True, max_length=100)),
                ('release_date', models.DateField(blank=True)),
                ('popularity', models.FloatField()),
                ('vote_average', models.FloatField(default=0)),
                ('adult', models.TextField(blank=True)),
                ('poster_path', models.TextField(blank=True)),
                ('overview', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TotalMovies',
            fields=[
                ('title', models.CharField(blank=True, max_length=100)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('genres', models.CharField(blank=True, max_length=100)),
                ('popularity', models.FloatField(blank=True)),
                ('release_date', models.DateField(blank=True)),
                ('runtime', models.CharField(blank=True, max_length=50)),
                ('adult', models.TextField(blank=True)),
                ('budget', models.IntegerField(default=0)),
                ('original_title', models.CharField(blank=True, max_length=100)),
                ('revenue', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('tagline', models.TextField(blank=True)),
                ('vote_average', models.FloatField(default=0)),
                ('vote_count', models.IntegerField(default=0)),
                ('video_id', models.CharField(max_length=500)),
                ('poster_path', models.TextField(blank=True)),
                ('backdrop_path', models.TextField(blank=True)),
                ('overview', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.totalmovies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
