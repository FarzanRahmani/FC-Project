# Generated by Django 3.1.3 on 2020-12-28 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_musics_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Karbar',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]