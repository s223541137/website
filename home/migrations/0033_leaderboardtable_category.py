# Generated by Django 4.2.14 on 2024-12-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_leaderboardtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboardtable',
            name='category',
            field=models.CharField(default='General', max_length=200),
            preserve_default=False,
        ),
    ]