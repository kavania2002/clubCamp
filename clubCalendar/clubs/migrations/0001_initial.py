# Generated by Django 3.1.7 on 2021-03-28 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=5000)),
                ('logged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('phoneNumber', models.IntegerField(null=True)),
                ('logged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sortDesc', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.TextField(max_length=2000)),
                ('image', models.TextField(max_length=5000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=100)),
                ('likes', models.IntegerField()),
                ('meet_link', models.TextField(max_length=2000)),
                ('clubName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.club')),
            ],
        ),
    ]
