# Generated by Django 4.2.2 on 2023-06-18 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_game_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gamespec',
        ),
    ]
