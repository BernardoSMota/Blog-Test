# Generated by Django 5.1.2 on 2024-11-12 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_likes_options_alter_likes_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
    ]