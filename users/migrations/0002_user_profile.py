# Generated by Django 4.1.2 on 2022-10-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]