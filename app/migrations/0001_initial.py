# Generated by Django 3.1.3 on 2021-07-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('points_submitted', models.CharField(max_length=255)),
                ('closest_point', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
    ]