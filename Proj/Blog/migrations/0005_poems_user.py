# Generated by Django 3.1.3 on 2020-12-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20201228_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='poems_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100, null=True)),
                ('poem', models.TextField(blank=True, max_length=100, null=True)),
                ('poet', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]